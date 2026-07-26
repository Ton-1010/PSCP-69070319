"""BrickBridge"""

a = int(input())
b = int(input())
goal = int(input())

use_b = min(b, goal // 5)
left_a = goal - (use_b * 5)

if left_a <= a:
    print(left_a)
else:
    print(-1)
