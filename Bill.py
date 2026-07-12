"""Bill"""

a = int(input())
b = a * 0.1
if b < 50:
   b=50
elif b > 1000:
   b = 1000
vat = (a + b) + ((a+b)*0.07)
print(f"{vat:.2f}")
