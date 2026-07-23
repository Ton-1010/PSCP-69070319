"""หาร10"""
number = int(input())
ans = number - (number % 10)
for i in range(ans, 0, -10):
    print(i,end=" ")
print(0)
