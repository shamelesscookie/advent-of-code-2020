input = open("input.txt")

raw_passes = []
boarding_passes = []

for line in input:
  raw_passes.append(line.strip())

for raw_pass in raw_passes:
  row = raw_pass[0:7]
  column = raw_pass[7:10]
  
  row = row.replace('F', '0')
  row = row.replace('B', '1')
  row = int(row, 2)
  
  column = column.replace('L', '0')
  column = column.replace('R', '1')
  column = int(column, 2)

  seat_id = row * 8 + column

  boarding_pass = {
    'row': row,
    'column': column,
    'seat_id': seat_id
  }

  boarding_passes.append(boarding_pass)
  
# part 1

boarding_passess_sorted_by_seat_id = sorted(boarding_passes, key=lambda item: item['seat_id'])
seat_numbers_sorted = []

for seat in boarding_passess_sorted_by_seat_id:
  seat_numbers_sorted.append(seat['seat_id'])

last_seat = seat_numbers_sorted[-1]

print('\nPart 1 Solution:')
print(last_seat)

# part 2 

first_seat = seat_numbers_sorted[0]

i = 0
for seat in range(first_seat, last_seat):
  if seat != seat_numbers_sorted[i]:
    your_seat = seat
    break
  i += 1

print('\nPart 2 Solution:')
print(your_seat)