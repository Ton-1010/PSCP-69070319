"""Shorten"""
numbers = []
while True:
    num = int(input())
    if num == -1:
        break
    numbers.append(num)
result = []
if numbers:
    start = numbers[0]
    end = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] == end + 1:
            end = numbers[i]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")
            start = numbers[i]
            end = numbers[i]
    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")
print(", ".join(result))
