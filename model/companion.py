import torch
import torch.nn as nn
import torch.nn.functional as F


class TransformerBlock(nn.Module):
    def __init__(self, embedding_dim, num_heads):
        super().__init__()

        self.ln1 = nn.LayerNorm(embedding_dim)

        self.attention = nn.MultiheadAttention(
            embed_dim=embedding_dim, num_heads=num_heads, batch_first=True
        )

        self.ln2 = nn.LayerNorm(embedding_dim)

        self.feed_forward = nn.Sequential(
            nn.Linear(embedding_dim, embedding_dim * 4),
            nn.GELU(),
            nn.Linear(embedding_dim * 4, embedding_dim),
        )

    def forward(self, x):
        T = x.size(1)

        # Causal Mask：禁止看到未来 token
        mask = torch.triu(
            torch.ones(T, T, device=x.device, dtype=torch.bool), diagonal=1
        )

        normalized = self.ln1(x)

        attention_output, _ = self.attention(
            normalized, normalized, normalized, attn_mask=mask, need_weights=False
        )

        x = x + attention_output

        x = x + self.feed_forward(self.ln2(x))

        return x


class CompanionModel(nn.Module):
    def __init__(
        self,
        vocab_size=8000,
        embedding_dim=256,
        num_heads=8,
        num_layers=4,
        max_seq_len=256,
    ):
        super().__init__()

        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.max_seq_len = max_seq_len

        # Embeddings
        self.token_embedding = nn.Embedding(vocab_size, embedding_dim)

        self.position_embedding = nn.Embedding(max_seq_len, embedding_dim)

        # Transformer
        self.blocks = nn.ModuleList(
            [TransformerBlock(embedding_dim, num_heads) for _ in range(num_layers)]
        )

        # Final normalization
        self.final_norm = nn.LayerNorm(embedding_dim)

        # 256 → 8000 logits
        self.lm_head = nn.Linear(embedding_dim, vocab_size, bias=False)

    def forward(self, token_ids, targets=None):
        B, T = token_ids.shape

        if T > self.max_seq_len:
            raise ValueError(
                f"Sequence length {T} exceeds max_seq_len {self.max_seq_len}"
            )

        positions = torch.arange(T, device=token_ids.device)

        # [B,T] → [B,T,256]
        x = self.token_embedding(token_ids) + self.position_embedding(positions)

        # Transformer Blocks
        for block in self.blocks:
            x = block(x)

        x = self.final_norm(x)

        # [B,T,256] → [B,T,8000]
        logits = self.lm_head(x)

        loss = None

        if targets is not None:
            loss = F.cross_entropy(
                logits.reshape(-1, self.vocab_size), targets.reshape(-1)
            )

        return logits, loss
