"""Giraffe"""
n = int(input())
heights = []
for _ in range(n):
    heights.append(int(input()))
if n == 1:
    print(1)
else:
    satisfied_count = 0
    for i in range(n):
        if not i:
            if heights[0] > heights[1]:
                satisfied_count += 1
        elif i == n - 1:
            if heights[n-1] > heights[n-2]:
                satisfied_count += 1
        else:
            if heights[i] > heights[i-1] and heights[i] > heights[i+1]:
                satisfied_count += 1
    print(satisfied_count)
