class Node:
  def __init__(self,data,next=None):
    self.data=data 
    self.next = next 
    
class Stack:
  def newNode(self,data):
    return Node(data)
  
  def traverse(self,head):
    if not head:
      return 
    print(head.data,end=" -> ")
    self.traverse(head.next)
    
  def push(self,head,data):
    if head is None:
      return self.newNode(data) 
    
    head.next = self.push(head.next,data)
    
  def pop(self,head):
    if not head.next:
      head = None 
      return 
    
    if not head.next.next:
      head.next = head.next.next 
      return 
    
    self.pop(head.next) 
  
  def peek(self,head):
    if not head.next:
      return head.data
    return self.peek(head.next) 
  
  def size(self,head):
    return 0 if not head else 1+self.size(head.next) 
  
 
head = Node(1)

stack = Stack() 
stack.push(head,5) 
print(stack.peek(head))
  
    