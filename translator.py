class Node:

   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
        
   def __str__(self):
      return ("Node({})".format(self.value)) 

   __repr__ = __str__

class Tree:

   def __init__(self):
      self.root = None

   def insert(self, value):
      if self.root is None:
         self.root=Node(value)
      else:
         self._insert(self.root, value)

   def _insert(self, node, value):
      if(value<node.value):
         if(node.left==None):
            node.left = Node(value)
         else:
            self._insert(node.left, value)
      else:   
         if(node.right==None):
            node.right = Node(value)
         else:
            self._insert(node.right, value)

class MorseTree(Tree):

   def __init__(self):
      super().__init__()

   def constructTree(self):
      self.insert('E')
      

