
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
  def reverseBetween(self,head,left,right):
    if left == right or head.next is None:
      return head 
    
    curr = head 
    prev = head
    startHead = None 
    i = 1 
    while i < left:
      curr = curr.next 
      prev = prev.next
      if startHead is None:
        startHead = head 
      else:
        startHead=startHead.next
        
      i+=1
      
    temp = prev 
    curr = curr.next 
    while i < right :
      next = curr.next 
      curr.next = prev 
      prev = curr 
      curr = next
      i+=1 
    
    temp.next = curr 
    if startHead:
      startHead.next = prev
    else:
      startHead = prev 
      head=startHead 
    return head
    


head = Node(1)
head.next = Node(2)
head.next.next= Node(3)
head.next.next.next= Node(4)
head.next.next.next.next= Node(5)
ans = Solution().reverseBetween(head,)

traverse(ans)