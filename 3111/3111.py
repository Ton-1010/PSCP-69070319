"""SAHAKORM"""
from decimal import Decimal, ROUND_HALF_UP
member = input()
all_price = Decimal("0")
num = int(input())
for _ in range(num):
    cost = Decimal(input())
    all_price += cost
if member == "Y":
    ans = all_price * Decimal("0.95")
elif member == "N" and all_price >= 500:
    ans = all_price * Decimal("0.97")
else:
    ans = all_price
final_ans = ans.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
print(f"{final_ans:.2f}")
