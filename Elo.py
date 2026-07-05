""""""
ra = int(input())
rb = int(input())
String = input()
import math
if String == "A":
   ea = 1 / ( 1 + math.pow(10, (rb - ra) / 400))
   print(f"{ea:.2f}")
elif String == "B":
   eb = 1 / (1 + math.pow(10, (ra - rb) / 400))
   print(f"{eb:.2f}")
