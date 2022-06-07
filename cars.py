from itertools import starmap
from collections import namedtuple

def cast(type, value):
  if type == 'INT':
    return int(value)
  if type == 'DOUBLE':
    return float(value)
  return str(value)

def cast_row(string, types=None):
  if types:
    return [*starmap(cast, zip(types, string.strip('\n').split(';')))];
  return string.strip('\n').split(';')
  
with open('./cars.csv') as file:
  file_iter = iter(file)
  header = cast_row(next(file_iter))
  data_types = cast_row(next(file_iter))
  Car = namedtuple('Car', header)

  cars = [Car(*cast_row(line, data_types))
          for line in file_iter]

print(cars)