class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_tree = BinarySearchTree(value) # Wrap the value in a new node
    if value > self.value: # Check if the new node's value is less than the current node's value
      
      if not self.right: # Check if there is no right child
        self.right = BinarySearchTree(value) # Put new node here
        # self.right = new_tree # Put new node here
      else:
        self.right.insert(value)

    else:
        if not self.left: # Check if there is no left child
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
      
    if target < self.value:
      if self.left is None:
        return False
      
      return self.left.contains(target)
      
    elif self.value < target:
      if self.right is None:
        return False
        
      return self.right.contains(target)

  def get_max(self):
    if self.right is None:
      return self.value
    
    return self.right.get_max()

  def for_each(self, cb):
    if self.left:
      self.left.for_each(cb)
    cb(self.value)

    if self.right:
      self.right.for_each(cb)