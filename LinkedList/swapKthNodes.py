class ListNode:
  def __init__(self,val=None,next=None):
    self.val = val 
    self.next = next 

  def length(self,head):
    if not head :
      return 0 
    return 1+self.length(head.next)
  
  
  def swapNodes(self,head,k):
    if not head or head.next is None:
      return head 
    
    if head.next.next is None:
      node = head.next
      temp = head 
      temp.next = head.next.next
      head = node
      head.next = temp
      return head
    
    front = None
    rear=None
    len = self.length(head)
    if k == len: k = 1 
    i=j=1 
    
    while i < k:
      if front is None:
       front = head 
       rear = head 
       j +=1 
      else:
        if j<=(len-k):
          rear = rear.next  
          j +=1 
        front=front.next 
      i +=1 
      
    
    while j <= (len-k):
      if rear is not None:
        rear = rear.next
      else:
        rear = head
      j +=1 
    
    if k == 1:
      frontNext = head.next
      front = head 
      front.next = rear.next.next
      head,rear.next = rear.next,head 
      head.next = frontNext
      rear.next = front  
      return head 
      
    rear.next,front.next = front.next,rear.next
    rear.next.next,front.next.next=front.next.next,rear.next.next 
    return head
