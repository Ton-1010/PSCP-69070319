"""isPrime_large"""
n = int(input())
if n <= 1:
    print("NO")
elif n == 2:
    print("YES")
elif not n % 2:
    print("NO")
else:
    Z = True
    limit = int(n ** 0.5)
    for i in range(3, limit + 1, 2):
        if not n % i:
            Z = False
            break
    if Z:
        print("YES")
    else:
        print("NO")
