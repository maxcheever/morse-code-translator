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
      self.root = Node('start')
      self.tree = self.morseTree
   
   @property
   def morseTree(self):

      #level1
      self.e = self.root.left = Node("E")
      self.t = self.root.right = Node("T")

      #level2
      self.i = self.e.left = Node("I")
      self.a = self.e.right = Node("A")
      self.n = self.t.left = Node("N")
      self.m = self.t.right = Node("M")

      #level3
      self.s = self.i.left = Node("S")
      self.u = self.i.right = Node("U")
      self.r = self.a.left = Node("R")
      self.w = self.a.right = Node("W")

      self.d = self.n.left = Node("D")
      self.k = self.n.right = Node("K")
      self.g = self.m.left = Node("G")
      self.o = self.m.right = Node("O")

      # level4
      self.h = self.s.left = Node("H")
      self.v = self.s.right = Node("V")
      self.f = self.u.left = Node("F")
      self.l = self.r.left = Node("L")
      self.p = self.w.left = Node("P")
      self.j = self.w.right = Node("J")

      self.b = self.d.left = Node("B")
      self.x = self.d.right = Node("X")
      self.c = self.k.left = Node("C")
      self.y = self.k.right = Node("Y")
      self.z = self.g.left = Node("Z")
      self.q = self.g.right = Node("Q")

def translatorHelper(node, char, code):
   if not node:
      return False
   elif node.value == char:
      return True
   else:
      if translatorHelper(node.left, char, code):
         code.insert(0, '.')
         return True
      elif translatorHelper(node.right, char, code):
         code.insert(0, '-')
         return True

def translator():
   morseCode = ''
   morseTree = Tree()
   for c in input('Enter A Message:\n'):
      translated = []
      if not c.isalpha():
         return 'Could Not Translate. Contains Unknown Characters'
      elif c.isalpha():
         translatorHelper(morseTree.root, c.upper(), translated)
         code = "".join(translated)
         morseCode = morseCode + code + " "

   return morseCode
      
print(translator())

