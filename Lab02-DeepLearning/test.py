import torch

# Create a tensor
x = torch.rand(2, 3)
print(x)

print(x.transpose(0, 1))
print(x.transpose(1, 0))
