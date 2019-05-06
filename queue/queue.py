class Node:
  def __init__(self, value = None, next_node = None):
    self.value = value
    self.next_node = next_node

  def get_data(self):
    return self.value
    
  def get_next(self):
    return self.next_node
    
  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_from_head(self):
    if not self.head or not self.tail:
      return None
    if self.head == self.tail:
      value = self.head.get_data()
      self.head = None
      self.tail = None
      return value
    else:
      old_head_value = self.head
      self.head = self.head.get_next()
      return old_head_value.get_data()

class Queue:
  def __init__(self):
    self.size = 0
 # what data structure should we
 # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    item = self.storage.remove_from_head()
    self.size = self.size - 1 if self.size > 0 else 0
    return item

  def len(self):
    return self.size

### Queues
#  * Should have the methods: `enqueue`, `dequeue`, and `len`.
#    * `enqueue` should add an item to the back of the queue.
#    * `dequeue` should remove and return an item from the front of the queue.
#    * `len` returns the number of items in the queue.