"""ของขวัญและขโมย"""
input_data = input().split()
n = int(input_data[0])
k = int(input_data[1])
t = int(input_data[2])
visited = set()
current = 1
visited.add(current)
while current != t:
    next_person = (current + k - 1) % n + 1
    visited.add(next_person)
    if next_person == 1:
        break
    current = next_person
print(len(visited))
