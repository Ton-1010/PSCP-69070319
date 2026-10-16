"""หุ่นยนต์เคาะเสียงกระเบื้อง"""
first_line = input().split()
N = int(first_line[0])
P = float(first_line[1])
col_tiles = [0] * N
col_points = [0] * N

total_tiles = 0
total_points = 0
row_outputs = []
for _ in range(N):
    row = list(map(int, input().split()))
    row_tiles_count = 0
    row_points_sum = 0

    for j in range(N):
        val = row[j]
        row_points_sum += val
        if val > 0:
            row_tiles_count += 1
            col_tiles[j] += 1
        col_points[j] += val
    total_tiles += row_tiles_count
    total_points += row_points_sum
    row_str = " ".join(map(str, row))
    row_outputs.append(f"{row_str} {row_tiles_count} {row_points_sum}")

for out in row_outputs:
    print(out)
print(" ".join(map(str, col_tiles)))
print(" ".join(map(str, col_points)))

total_fine = total_points * P
print(f"{total_tiles} {total_points} {total_fine:.2f}")
