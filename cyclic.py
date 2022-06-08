class CyclicIterator:
  def __init__(self, list_):
    self._list = list_
    self._index = 0

  def __len__(self):
    return len(self._list)

  def __iter__(self):
    return self

  def __next__(self):
    result = self._list[self._index % len(self)]
    self._index += 1
    return result


cyclic = CyclicIterator('NSWE')

# for item in cyclic:
#   print(item)

# //////////

class CyclicIterator:
  def __init__(self, list_, long_):
    self._list = list_
    self._index = 0
    self._long = long_

  def __len__(self):
    return len(self._list)

  def __iter__(self):
    return self

  def __next__(self):
    if self._index >= self._long:
      raise StopIteration
    result = self._list[self._index % len(self)]
    self._index += 1
    return result


cyclic = CyclicIterator('NSWE', 10)

# for item in cyclic:
#   print(item)

# //////////

class CyclicIterator:
  def __init__(self, list_):
    self._list = list_
    self._index = 0

  def __len__(self):
    return len(self._list)

  def __iter__(self):
    return self

  def __next__(self):
    result = self._list[self._index % len(self)]
    self._index += 1
    return result


cyclic = CyclicIterator('NSWE')

# results = []
# for i in range(10):
#   results.append(f'{i+1}{next(cyclic)}')
# print(results)

# results = [f'{i+1}{next(cyclic)}' for i in range(10)]
# print(results)

import itertools

cyclic = itertools.cycle('NSWE')

# results = [f'{index+1}{direction}' for index, direction in zip(range(10), cyclic)]
# print(results)

# //////////

class CyclicIterator:
  def __init__(self, iterable):
    self.iterable = iterable
    self.iterator = iter(self.iterable)

  def __len__(self):
    return len(self.iterable)

  def __iter__(self):
    return self

  def __next__(self):
    try:
      return next(self.iterator)
    except StopIteration:
      self.iterator = iter(self.iterable)
      return next(self.iterator)


cyclic = CyclicIterator('NSWE')

results = [f'{index+1}{direction}' for index, direction in zip(range(10), cyclic)]
print(results)
