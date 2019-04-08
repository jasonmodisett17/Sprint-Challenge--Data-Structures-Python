class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < len(self.storage) - 1:
      self.storage[self.current] = item
      self.current += 1

    else:
      self.storage[self.current] = item
      self.current = 0

  def get(self):
    return [x for x in self.storage if x]