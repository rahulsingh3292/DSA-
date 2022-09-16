
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
  def oddEvenListN(self,head):
    if not head or not head.next or not head.next.next:
      return head 
    odd=even=odd_next=even_next=None
    temp = head.next
    curr = head 
    while curr and curr.next:
      if odd is None:
        odd = Node(curr.val)
        odd_next=odd 
      else:
        node = Node(curr.val)
        odd_next.next = node 
        odd_next = node 
      curr=curr.next.next 
    if curr:
      odd_next.next = curr 
      odd_next = curr
    
    curr=temp
    while curr and curr.next:
      if even is None:
        even = Node(curr.val)
        even_next=even
      else:
        node = Node(curr.val)
        even_next.next = node 
        even_next = node 
      curr=curr.next.next 
    if curr:
      even_next.next = curr 
    odd_next.next = even
    return odd
   
class Solution:
  def oddEvenList(self,head):
    if not head or not head.next or not head.next.next:
      return head 
    
    even=even_next = None 
    odd=odd_next = None 
    curr = head 
    while curr and curr.next:
      if odd is None:
        odd = curr 
        odd_next=odd 
      else:
        odd_next.next = curr 
        odd_next= odd_next.next 
        
      if even is None:
        even = curr.next 
        even_next = even 
      else:
        even_next.next = curr.next 
        even_next = even_next.next
      
      curr = curr.next.next
      
    
    if curr:
      temp = curr.next
      odd_next.next = curr
      curr.next = even 
      even_next.next =temp 
      return odd
    
    else:
      odd_next.next = even 
      even_next.next = curr 
      return odd
      
  
  

head = Node(1) 
head.next = Node(2) 
head.next.next= Node(3)  
head.next.next.next = Node(4)
head.next.next.next.next= Node(5)
head.next.next.next.next.next= Node(6)

res = Solution().oddEvenList(head)
traverse(res)