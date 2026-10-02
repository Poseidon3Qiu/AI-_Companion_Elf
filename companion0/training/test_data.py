import sys
import torch
from tokenizers import Tokenizer

sys.path.append("model")
from companion import CompanionModel


# 1. 加载 tokenizer
tokenizer = Tokenizer.from_file("tokenizer/tokenizer_v0.json")

# 2. 读取真实 TinyStories
with open("data/processed/tinystories_50k.txt", "r", encoding="utf-8") as f:
    text = f.read(5000)

# 3. Text → Token IDs
token_ids = tokenizer.encode(text).ids

# 4. 取连续 257 个 tokens
sequence = torch.tensor(token_ids[:257], dtype=torch.long)

# 5. 制作 next-token prediction 数据
inputs = sequence[:-1].unsqueeze(0)
targets = sequence[1:].unsqueeze(0)

# 6. 创建 Companion-0
model = CompanionModel()

# 7. Forward
logits, loss = model(inputs, targets)

print("inputs shape:", inputs.shape)
print("targets shape:", targets.shape)
print("logits shape:", logits.shape)
print("loss:", loss.item())
