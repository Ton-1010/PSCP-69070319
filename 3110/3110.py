"""สงคราม...ส่งด่วน"""
X = input()
Y = X.split(" ")
s = Y[0]
e = Y[1]
kg = float(input())

if s == "BKK" and e == "CNX":
    print(f"{10 + (30 * kg):.2f}")
elif s == "CNX" and e == "UBP":
    print(f"{15 + (40 * kg):.2f}")
elif s == "UBP" and e == "BKK":
    print(f"{20 + (40 * kg):.2f}")
elif s == "BKK" and e == "PTK":
    print(f"{25 + (50 * kg):.2f}")
elif s == "PKT" and e == "CNX":
   print(f"{30 + (60 * kg):.2f}")
elif s == "UBP" and e == "PKT":
    print(f"{40 + (70 * kg):.2f}")
else:
    print("Error")
