import torch

w = torch.tensor(5.0, requires_grad=True)

x = torch.tensor(2.0)
target = torch.tensor(8.0)

learning_rate = 0.01
optimizer = torch.optim.SGD([w], lr=learning_rate)

for step in range(20):
    # 1. Forward
    prediction = x * w

    # 2. Loss
    loss = (prediction - target) ** 2

    # 3. Backpropagation
    loss.backward()

    optimizer.step()

    optimizer.zero_grad()

    print("step =", step, "w =", round(w.item(), 4), "loss =", round(loss.item(), 4))
