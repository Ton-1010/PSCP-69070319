"""Temperature"""
TEMP_VALUE = float(input())
FROM_UNIT = input().strip().upper()
TO_UNIT = input().strip().upper()

if FROM_UNIT == 'C':
    CELSIUS = TEMP_VALUE
elif FROM_UNIT == 'K':
    CELSIUS = TEMP_VALUE - 273.15
elif FROM_UNIT == 'F':
    CELSIUS = (TEMP_VALUE - 32) * 5 / 9
elif FROM_UNIT == 'R':
    CELSIUS = (TEMP_VALUE * 5 / 9) - 273.15
else:
    CELSIUS = 0.0

if TO_UNIT == 'C':
    RESULT = CELSIUS
elif TO_UNIT == 'K':
    RESULT = CELSIUS + 273.15
elif TO_UNIT == 'F':
    RESULT = (CELSIUS * 9 / 5) + 32
elif TO_UNIT == 'R':
    RESULT = (CELSIUS + 273.15) * 9 / 5
else:
    RESULT = 0.0
print(f"{RESULT:.2f}")
