"""INK"""
PI = 3.1416
s,n = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    r_squared = x ** 2 + y ** 2
    area_needed = PI * r_squared
    time_needed = area_needed / s
    ans = int(time_needed)
    if time_needed > ans:
        ans += 1
    print(ans)
