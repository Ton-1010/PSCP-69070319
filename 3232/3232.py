"""กบน้อยกระโดด"""
X, Y = map(int, input().split())
total_distance = 0
current_jump = X
jump = 0
while total_distance < Y:
    if current_jump <= 0:
        print(-1)
        break
    total_distance += current_jump
    current_jump -= 2
    jump += 1
else:
    print(jump)
