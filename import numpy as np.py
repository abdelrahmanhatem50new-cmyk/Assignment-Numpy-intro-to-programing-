import numpy as np

# ---------- Task 1 ----------
print("Task 1")
arr = np.random.randint(1, 100, (3, 3))
print("original array:")
print(arr)

mn = arr.min()
mx = arr.max()

norm = (arr - mn) / (mx - mn)
print("normalized array:")
print(norm)
print()

# ---------- Task 2 ----------
print("Task 2")
a = np.random.randint(1, 20, 10)
print("array:", a)

x = input("Enter a value X: ")

diff = abs(a - x)
index = np.argmin(diff)
print("closest value to X is:", a[index])
print()

# ---------- Task 3 ----------
print("Task 3")
b = np.random.randint(1, 50, (5, 5))
print(b)

result = []
for i in range(5):
    col = b[:, i]
    col = sorted(col)
    result.append(col[1])      # second value
print("second largest of each column:", result)
print()

# ---------- Task 4 ----------
print("Task 4")
m = np.random.randint(1, 10, (6, 4))
print(m)

for i in range(6):
    s = m[i].sum()
    if s % 2 == 0:
        print("row", i, "has even sum")
print()

# ---------- Task 5 ----------
print("Task 5")
c = np.random.randint(1, 50, 30)
print("before:", c)

for i in range(len(c)):
    if c[i] % 3 == 0 and c[i] % 5 == 0:
        c[i] = -1
print("after:", c)
print()

# ---------- Task 6 ----------
print("Task 6")
d = np.random.randint(1, 30, (3, 3))
print("before:")
print(d)

for i in range(3):
    mean = d[i].mean()
    d[i] = d[i] - mean
print("after:")
print(d)