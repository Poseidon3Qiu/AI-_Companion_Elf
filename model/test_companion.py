import torch
from companion import CompanionModel


model = CompanionModel()

# 假装这是 tokenizer 输出的一小段 Token IDs
inputs = torch.tensor([[10, 25, 300, 42], [8, 91, 17, 6]])

# Next-token prediction 的正确答案
targets = torch.tensor([[25, 300, 42, 100], [91, 17, 6, 200]])

logits, loss = model(inputs, targets)

print("inputs shape:", inputs.shape)
print("logits shape:", logits.shape)
print("loss:", loss.item())

# 统计模型参数量
num_params = sum(p.numel() for p in model.parameters())

print("parameters:", f"{num_params:,}")
