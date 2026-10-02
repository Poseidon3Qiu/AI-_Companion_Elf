import sys
import torch
from tokenizers import Tokenizer

sys.path.append("model")
from companion import CompanionModel


# -------------------------
# Device
# -------------------------

if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

print("Device:", device)


# -------------------------
# Tokenizer
# -------------------------

tokenizer = Tokenizer.from_file("tokenizer/tokenizer_v0.json")


# -------------------------
# Load Model
# -------------------------

model = CompanionModel().to(device)

model.load_state_dict(torch.load("companion_0_checkpoint.pt", map_location=device))

model.eval()


# -------------------------
# Starting Prompt
# -------------------------

prompt = "Once upon a time"

token_ids = tokenizer.encode(prompt).ids

generated = torch.tensor([token_ids], dtype=torch.long, device=device)


# -------------------------
# Generate
# -------------------------

MAX_NEW_TOKENS = 50

with torch.no_grad():
    for _ in range(MAX_NEW_TOKENS):
        # 最多只保留最近 256 tokens
        context = generated[:, -256:]

        # Forward
        logits, _ = model(context)

        # 只看最后一个位置对“下一个 token”的预测
        next_token_logits = logits[:, -1, :]

        # 转成概率
        probabilities = torch.softmax(next_token_logits, dim=-1)

        # 按概率抽取下一个 token
        next_token = torch.multinomial(probabilities, num_samples=1)

        # 接到已有 sequence 后面
        generated = torch.cat([generated, next_token], dim=1)


# -------------------------
# Decode
# -------------------------

output_ids = generated[0].tolist()

text = tokenizer.decode(output_ids)

print("\n--- Generated Text ---\n")
print(text)
