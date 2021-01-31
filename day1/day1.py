input = open("input.txt")

numbers = []

for line in input:
  numbers.append(int(line))

# part 1
for x in numbers:
  diff = 2020 - x
  try:
    y_index = numbers.index(diff)
  except ValueError:
    continue
  print('\nPart 1 Solution:')
  print(f'x = {x}')
  print(f'y = {numbers[y_index]}')
  print(f'x + y = {x + numbers[y_index]}')
  print(f'x * y = {x * numbers[y_index]}')
  break

# part 2
for x in numbers:
  diff = 2020 - x
  for y in numbers:
    diff2 = diff - y
    try:
      z_index = numbers.index(diff2)
    except ValueError:
      continue
    print('\nPart 2 Solution:')
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {numbers[z_index]}')
    print(f'x + y + z = {x + y + numbers[z_index]}')
    print(f'x * y * z = {x * y * numbers[z_index]}')
    break
  else:
    continue
  break