class Solution:
  
  # Extra space O(N) for stack.. 
  def stack(self,head):
    stack = list()
    slow=fast= head 
    while fast is not None and fast.next is not None:
      fast = fast.next.next 
      slow = slow.next 
    
    while slow is not None:
      if not fast:
        if slow is not None:
          stack.append(slow)
      else:
          if slow.next is not None:
            stack.append(slow.next)
        
      slow = slow.next
    return stack 
  
  def reorderList(self,head):
    stack = self.stack(head)
    curr = head 
 
    while stack and curr is not None:
      nthNode = stack.pop() 
      nthNode.next = curr.next  
      curr.next = nthNode 
      curr = curr.next.next
    curr.next = None
    return head

  # Using O(1) space.. 
  def reorderList(self,head):
    slow=fast = head 
    while fast and fast.next:
      fast=fast.next.next 
      slow=slow.next 
    
    if fast:
      fast = slow.next
    else:
      fast = slow
    
 
   # reverse the list
    curr,prev = fast ,None
    while curr:
      next = curr.next
      curr.next = prev 
      prev = curr 
      curr=next 
    fast = prev 
   
    prev = head
    curr = fast 
    
    while curr:
      next = curr.next 
      temp = curr 
      temp.next = prev.next 
      prev.next = temp 
      prev = prev.next.next 
      curr = next
    prev.next = curr
    
    
    
    
    

class Node:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 

head = Node(1)
head.next= Node(2)

head.next.next= Node(3)
head.next.next.next = Node(4)
"""
head.next.next.next.next= Node(5) 
head.next.next.next.next.next= Node(6) 
"""


ans = Solution().reorder(head)

def traverse(head):
  if not head:
    return 
  print(head.val,end=" ")
  traverse(head.next)

traverse(head)