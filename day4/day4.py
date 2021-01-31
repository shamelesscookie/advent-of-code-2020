import re

input = open("input.txt")

records = []

record = {}

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for line in input:
  if line == '\n':
    records.append(record)
    record = {}
    continue
  
  for field in fields:
    field_expression = re.compile(f'.*{field}:([^\s]+)')
    matching_fields = field_expression.match(line)
    try:
      field_value = matching_fields.group(1)
      record[field] = field_value
    except AttributeError:
      continue

# part 1
num_valid_records = 0

def has_required_fields(record):
  for required_field in required_fields:
    if not required_field in record:
      return False
  return True

for record in records:
  if has_required_fields(record):
    num_valid_records += 1

print('\nPart 1 Solution:')
print(num_valid_records)


# part 2
def is_valid_byr(byr):
  try:
    int(byr)
  except ValueError:
    return False
  if (int(byr) < 1920) or (int(byr) > 2002):
    return False
  return True

def is_valid_iyr(iyr):
  try:
    int(iyr)
  except ValueError:
    return False
  if (int(iyr) < 2010) or (int(iyr) > 2020):
    return False
  return True

def is_valid_eyr(eyr):
  try:
    int(eyr)
  except ValueError:
    return False
  if (int(eyr) < 2020) or (int(eyr) > 2030):
    return False
  return True

def is_valid_hgt(hgt):
  expr = re.compile('^([\d]+)(cm|in)$')
  matches = expr.match(hgt)
  try:
    height = int(matches.group(1))
    units = matches.group(2)
  except AttributeError:
    return False
  except ValueError:
    return False
  if (units == 'cm') and ((height < 150) or (height > 193)):
    return False
  if (units == 'in') and ((height < 59) or (height > 76)):
    return False
  return True

def is_valid_hcl(hcl):
  expr = re.compile('^(#[0-9a-f]{6})$')
  matches = expr.match(hcl)
  try:
    matches.group(1)
  except AttributeError:
    return False
  return True

def is_valid_ecl(ecl):
  valid_ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  try:
    valid_ecls.index(ecl)
  except ValueError:
    return False
  return True

def is_valid_pid(pid):
  expr = re.compile('^([\d]{9})$')
  matches = expr.match(pid)
  try:
    matches.group(1)
  except AttributeError:
    return False
  return True

def is_valid_record(record):
  if has_required_fields(record):
    if is_valid_byr(record['byr']):
      if is_valid_ecl(record['ecl']):
        if is_valid_eyr(record['eyr']):
          if is_valid_hcl(record['hcl']):
            if is_valid_hgt(record['hgt']):
              if is_valid_iyr(record['iyr']):
                if is_valid_pid(record['pid']):
                  return True
  return False

num_valid_records = 0
  
for record in records:
  if is_valid_record(record):
    num_valid_records += 1

print('\nPart 2 Solution:')
print(num_valid_records)