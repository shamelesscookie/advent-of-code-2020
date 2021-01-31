import re

input = open("input.txt")

lines = []

for line in input:
  lines.append(line)

# part 1
num_valid_passwords = 0

for line in lines:
  sample = re.compile('(\d+)-(\d+)\s([a-z]):\s([a-z]+)')
  match = sample.match(line)
  minimum = int(match.group(1))
  maximum = int(match.group(2))
  character = match.group(3)
  password = match.group(4)
  
  count = password.count(character)
  
  if (count >= minimum) and (count <= maximum):
    num_valid_passwords += 1

print('\nPart 1 Solution:')
print(num_valid_passwords)

# part 2
num_valid_passwords = 0

for line in lines:
  sample = re.compile('(\d+)-(\d+)\s([a-z]):\s([a-z]+)')
  match = sample.match(line)
  first_position = int(match.group(1))
  second_position = int(match.group(2))
  character = match.group(3)
  password = match.group(4)
  
  first_match = password[first_position-1] == character
  second_match = password[second_position-1] == character

  if (first_match ^ second_match):
    num_valid_passwords += 1

print('\nPart 2 Solution:')
print(num_valid_passwords)