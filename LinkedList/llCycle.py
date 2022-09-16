class Solution:
  def detectCycle(self,head):
    visited = {} 
    
    curr = head
    while curr is not None:
      if not visited.get(curr):
        visited[curr]  = True 
      else:
        return curr
      curr = curr.next 
    return -1
  
  # using floyd cycle detection 
  # O(1) space
  def detectCycle(self,head):
    slow=fast=head 
    while fast!=None and fast.next != None:
      fast = fast.next.next 
      slow = slow.next 
      if slow == fast:
        break 
    if not fast or fast.next is None:
      return 
    
    slow = head 
    while slow!=fast:
      slow=slow.next 
      fast=fast.next
    
    return None if not slow or slow.next is None else slow 
    
    

class Node:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 
"""
1 -> 2 -> 3 -> 4 -> 6 
          |         |
          9 <- 8 <- 7
                
"""