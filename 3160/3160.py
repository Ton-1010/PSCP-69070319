"""หาจำนวนเฉพาะ"""
s , e = map(int, input().split())
primes = []

for k in range(s, e + 1):
    if k > 1:
        is_prime = True
        for i in range(2, int(k**0.5) + 1):
            if not k % i :
                is_prime = False
                break
        if is_prime:
            primes.append(k)
for l in primes:
    if l != primes[-1]:
        print(l, end=" ")
    else:
        print(l)
print(f"Total primes: {len(primes)}")
