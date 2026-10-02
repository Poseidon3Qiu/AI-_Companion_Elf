import sys
import torch
from tokenizers import Tokenizer

sys.path.append("model")
from companion import CompanionModel


# -------------------------
# Configuration
# -------------------------

SEQ_LEN = 256
BATCH_SIZE = 8
TRAIN_STEPS = 10
LEARNING_RATE = 3e-4


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
# Training Data
# -------------------------

print("Loading TinyStories...")

with open("data/processed/tinystories_50k.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Tokenizing...")

token_ids = tokenizer.encode(text).ids

data = torch.tensor(token_ids, dtype=torch.long)

print("Total tokens:", len(data))


# -------------------------
# Model
# -------------------------

model = CompanionModel().to(device)

num_params = sum(p.numel() for p in model.parameters())

print("Parameters:", f"{num_params:,}")


# -------------------------
# Optimizer
# -------------------------

optimizer = torch.optim.AdamW(model.parameters(), lr=LEARNING_RATE)


# -------------------------
# Batch Generator
# -------------------------


def get_batch():

    max_start = len(data) - SEQ_LEN - 1

    starts = torch.randint(0, max_start, (BATCH_SIZE,))

    inputs = torch.stack([data[start : start + SEQ_LEN] for start in starts])

    targets = torch.stack([data[start + 1 : start + SEQ_LEN + 1] for start in starts])

    return inputs.to(device), targets.to(device)


# -------------------------
# Training Loop
# -------------------------

print("\nStarting training...\n")

model.train()

for step in range(1, TRAIN_STEPS + 1):
    inputs, targets = get_batch()

    optimizer.zero_grad()

    logits, loss = model(inputs, targets)

    loss.backward()

    optimizer.step()

    if step == 1 or step % 10 == 0:
        print(f"Step {step:4d} | Loss {loss.item():.4f}")


# -------------------------
# Save Checkpoint
# -------------------------

torch.save(model.state_dict(), "companion_0_checkpoint.pt")

print("\nTraining complete.")
print("Checkpoint saved: companion_0_checkpoint.pt")
