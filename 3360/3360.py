"""หั่นขนมปัง"""
W, H, _, _ = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
X = [0] + X + [W]
Y = [0] + Y + [H]
widths = []
for i in range(len(X) - 1):
    widths.append(X[i+1] - X[i])
heights = []
for i in range(len(Y) - 1):
    heights.append(Y[i+1] - Y[i])
widths.sort(reverse=True)
heights.sort(reverse=True)
max1 = widths[0] * heights[0]
max2 = max(widths[0] * heights[1], widths[1] * heights[0])
print(max1, max2)
