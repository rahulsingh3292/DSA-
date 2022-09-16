

class Node:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 
  
class Queue:
  def __init__(self):
    self.front=self.rear= None 
  
  def enque(self,val):
    if not self.front:
      self.rear=self.front = Node(val)
      return 
    node = Node(val)
    self.rear.next = node
    self.rear = node
    
  def deque(self):
    self.front = self.front.next 
    return 
  def isEmpty(self):
    return not self.front 
    
  def traverse(self,head):
    if not head:
      return 
    print(head.val,end=" -> ")
    self.traverse(head.next)

Q = Queue()
Q.enque(1)
Q.enque(2)
Q.deque()
Q.deque()
print(Q.isEmpty())
Q.traverse(Q.front)
  
 
