import torch
import numpy as np

a = torch.ones(5)
print(a)

a_np = np.array([0.5, 0.4, 2])
print(a_np)

b_tensor = torch.tensor(a_np)
print(b_tensor)

b = a.numpy()
print(b)

print(type(b))
print(type(a))

if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5, device=device)
    print(x)
    # z = x.numpy()
    # print(z)

if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5, device=device)
    print(x)
    x = x.to("cpu")
    print(x)
    z = x.numpy()
    print(z)
