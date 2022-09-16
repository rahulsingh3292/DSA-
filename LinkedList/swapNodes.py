class ListNode:
  def __init__(self,val=None,next=None):
    self.val = val 
    self.next = next
    
  def swapPairs(self,ll):
    curr = ll 
    prev = None 
    
    while curr is not None and curr.next is not None:
      next = curr.next 
      temp = curr 
      
      if prev is None:
        ll = next 
        temp.next = next.next
        ll.next = temp 
        prev = ll.next
        curr = curr.next
      else:
        nextNode = next.next 
        prev.next = next 
        prev.next.next = temp
        temp.next = nextNode 
        prev = temp 
        curr = temp.next
   
    return ll

  def swap(self,head):
    curr = head 
    prev = None
    while curr != None and  curr.next != None:
      next = curr.next.next 
      if prev is None:
        curr,curr.next = curr.next,curr
        curr.next.next = next 
        head = curr 
        prev = curr.next
        curr = next
      else:
        curr,curr.next = curr.next,curr 
        curr.next.next = next
        prev.next = curr
        prev = curr.next
        curr = next 

    return head