"""ปราสาท"""
n = int(input())
if n == 1:
    print(0)
else:
    row = int(n ** 0.5)
    if row * row < n:
        row += 1
    start_of_row = (row - 1) ** 2 + 1
    idx = n - start_of_row + 1
    if not idx % 2 :
        ans = 2 * row - 3
    else:
        ans = 2 * row - 2
    print(ans)
