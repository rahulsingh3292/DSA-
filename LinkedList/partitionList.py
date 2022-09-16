
class Node:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 

def traverse (head):
  if not head:
    return 
  print(head.val,end=" -> ")
  traverse(head.next)

class Solution:
  
  def partition(self,head,x):
    if not head or (not head.next) or (x< -100):
      return head
    
    front=rear=None 
    front_next,rear_next= front,rear
    curr = head 
    while curr:
      if curr.val < x: 
        if not front:
          front = ListNode(curr.val)
          front_next = front 
        else:
          node = ListNode(curr.val)
          front_next.next = Node 
          front_next=node 
      else:
        if not rear:
          rear = ListNode(curr.val) 
          rear_next = rear 
        else:
          node = ListNode(curr.val)
          rear_next.next = node 
          rear_next= node 
      curr = curr.next
      
    if not front:
      return rear 
    front_next.next = rear
    return front 
  
  
    
      



head = Node(1) 
head.next = Node(4) 
head.next.next= Node(3)  
head.next.next.next = Node(2)
head.next.next.next.next= Node(5)
head.next.next.next.next.next = Node(2) 
x = 3
res = Solution().partition(head,x)
traverse(res)