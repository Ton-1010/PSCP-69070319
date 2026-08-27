"""A-E-I-O-U"""
z = ["a", "e", "i", "o", "u"]
x = input().lower()

for i in (x):
    if i == z[0]:
        z[0] += 1
    elif i == z[1]:
        z[1] += 1
    elif i == z[1]:
        z[2] += 1
    elif i == z[1]:
        z[3] += 1
    elif i == z[1]:
        z[4] += 1
print(z)
