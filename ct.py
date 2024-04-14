from time import time;from tqdm import tqdm
t = int(input("Enter level: ")) * 10000 + 1
s = time()
a = {i*i:i for i in range(1,t)}
z = []
for i in tqdm(range(1,t)):
    for j in range(i,t):
        c = i * i + j * j
        if c in a:
            z.append([i,j,a[c]])
b = time()
print(f"Used {b - s} second,Level {int(t/50000)}")