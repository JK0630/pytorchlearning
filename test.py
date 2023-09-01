import torch
import torch.nn as nn

print(torch.cuda.is_available())

x = torch.Tensor([1, 2, 3, 4, 5]).to('cuda:0')
y = torch.Tensor([1, 2, 3, 4, 5]).to('cpu')

print(x)
print(y)