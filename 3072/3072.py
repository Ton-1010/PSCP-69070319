"""A-E-I-O-U"""
a = input().lower()
vowels = ["a", "e", "i", "o", "u"]
counts = [0, 0, 0, 0, 0]
for i in range(5):
    counts[i] = a.count(vowels[i])
for i in range(5):
    if counts[i] > 0:
        print(f"{vowels[i]} : {counts[i]}")
