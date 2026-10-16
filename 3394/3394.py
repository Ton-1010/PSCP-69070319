"""ส่งต่อ"""
N, S = map(int, input().split())
next_student = [0] * (N + 1)
for i in range(1, N + 1):
    next_student[i] = int(input())
visited = set()
current = S
while current and current not in visited:
    visited.add(current)
    current = next_student[current]
print(len(visited))
