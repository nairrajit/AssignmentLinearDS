# Write a program to find the smallest number using a stack

class MinStack():
   min=float('inf')
   def __init__(self):
      self.min=float('inf')
      self.stack = []
   def push(self, x):
      if x<=self.min:
         self.stack.append(self.min)
         self.min = x
      self.stack.append(x)
   def top(self):
      return self.stack[-1]
   def getMin(self):
      return self.min

m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
m.push(100)
m.push(-50)
m.push(60)
print("Smallest number: ",m.getMin())