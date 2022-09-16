class Stack(object):
  
  def __init__(self):
    self.stack = list() 
  
  def push(self,n):
    self.stack.append(n) 
  
  def pop(self):
    self.stack.pop() 
    
  def peek(self):
    return self.stack[-1] 
  
  def isEmpty(self):
    return not self.stack 
  
  def size(self):
    return len(self.stack)
  
from collections import deque 

stack = deque() 

stack.append(5)
stack.append(7)
stack.append(9)
stack.append(4) 
stack.appendleft(7) 
stack.popleft()
import time
for m in dir(stack):
  print(m)
  time.sleep(0.5)