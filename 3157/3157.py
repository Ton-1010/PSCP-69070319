"""เกมสะสมแต้ม"""
n = int(input())
score = 0
for _ in range(n):
    command = input()
    if command == "+":
        score += 10
    elif command == "-":
        score -= 5
print(score)
