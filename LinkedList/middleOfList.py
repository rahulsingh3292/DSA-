class ListNode:
  def __init__(self,val=None,next=None):
    self.val = val 
    self.next = next 
  
  def length(self,ll):
    if ll is None:
      return 0 
    return 1+self.length(ll.next)
  
  
  def middleNode(self,head):
    mid = self.length(head)//2 
    i=0
    curr = head
    while i!=mid:
      curr = curr.next 
      i+=1
    return curr 
  
  def traverse (self,ll):
    if not ll:
      return 
    print(ll.val,end=" ")
    self.traverse(ll.next)

ll = ListNode(3) 
ll.next = ListNode(0)
ll.next.next = ListNode(2) 
ll.next.next.next = ListNode(6) 
ll.next.next.next.next = ListNode(8) 
ll.next.next.next.next.next = ListNode(1) 
ll.next.next.next.next.next.next= ListNode(7) 
ll.next.next.next.next.next.next.next= ListNode(9) 
ll.next.next.next.next.next.next.next.next= ListNode(4) 
ll.next.next.next.next.next.next.next.next.next= ListNode(5) 
ll.next.next.next.next.next.next.next.next.next.next= ListNode(2) 
ll.next.next.next.next.next.next.next.next.next.next.next= ListNode(5) 
ll.next.next.next.next.next.next.next.next.next.next.next.next= ListNode(0) 
