"""B - Fully pair?"""
z = input().strip()
char_count = {}
for char in z:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
unpaired_chars = []
seen = set()
for char in z:
    if char not in seen:
        seen.add(char)
        if char_count[char] % 2:
            unpaired_chars.append(char)
if not unpaired_chars:
    print("fully paired")
else:
    print("".join(unpaired_chars))
