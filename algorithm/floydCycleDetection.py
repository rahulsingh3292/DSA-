class Detect:
  # for linked list cycle detection.. 
  
  def hasCycle(self,head):
    slow=fast=head 
    while fast!=None and fast.next != None:
      fast = fast.next.next 
      slow = slow.next 
      if slow == fast:
        return True 
    return False 
    