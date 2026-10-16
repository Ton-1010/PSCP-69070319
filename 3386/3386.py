"""Duplicate I"""
m = int(input())
n = int(input())
group1 = set()
for _ in range(m):
    group1.add(int(input()))
common = set()
for _ in range(n):
    student_id = int(input())
    if student_id in group1:
        common.add(student_id)
if not common:
    print("Nope")
else:
    result = sorted(list(common), reverse=True)
    for student_id in result:
        print(student_id)
