import re

input = open("input.txt")

groups = []

group = []

for line in input:
  if line == '\n':
    groups.append(group)
    group = []
    continue
  
  group.append(line.strip())

# part 1

total_yes = 0

for g in groups:
  distinct_yes = {}
  for person in g:
    for yes in list(person):
      distinct_yes[yes] = True
  total_yes += len(distinct_yes)

print('\nPart 1 Solution:')
print(total_yes)


# part 2

total_yes = 0

for g in groups:
  first_person = g[0]
  for q in first_person:
    consensus = True
    for person in g:
      try:
        person.index(q)
      except ValueError:
        consensus = False
        break

    if consensus:
      total_yes += 1

print('\nPart 2 Solution:')
print(total_yes)