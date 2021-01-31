input = open("input.txt")

lines = []

for line in input:
  lines.append(line)

# part 1
x = 0
y = 0

x_position = 0
num_trees = 0

x_increment = 3
y_increment = 1

iterations = int(len(lines))

for i in range(0, iterations-1, y_increment):
  x += x_increment
  y += y_increment

  x_position = x % (len(lines[y]) - 1)

  if (lines[y][x_position] == '#'):
    num_trees += 1

print('\nPart 1 Solution:')
print(num_trees)

# part 2
x_increments = [1, 3, 5, 7, 1]
y_increments = [1, 1, 1, 1, 2]

trees_per_slope = []

for s in range(0, len(x_increments)):
  x = 0
  y = 0
  x_position = 0
  num_trees = 0

  x_increment = x_increments[s]
  y_increment = y_increments[s]

  iterations = int(len(lines))
  
  # print(f'x_increment {x_increment}, y_increment {y_increment}, iterations {iterations}')

  for i in range(0, iterations-1, y_increment):
    x += x_increment
    y += y_increment

    x_position = x % (len(lines[y]) - 1)

    # print(f'Ln {y+1}, Col {x+1}, x {x}, len {len(lines[y]) - 1}, x_position {x_position}: {lines[y][x_position]}')

    if (lines[y][x_position] == '#'):
      num_trees += 1

  trees_per_slope.append(num_trees)

compound_trees = 1

for trees in trees_per_slope:
  compound_trees *= trees

print('\nPart 2 Solution:')
print(compound_trees)