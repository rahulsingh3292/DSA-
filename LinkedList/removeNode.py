class ListNode:
  def __init__(self,val=None,next=None):
    self.val = val 
    self.next = next 
  
  def length(self,ll):
    if ll is None:
      return 0 
    return 1+self.length(ll.next)
  
  def solve(self,ll,n,i=1):
    if i==n:
      next = ll.next.next 
      ll.next = next
      return 
    self.solve(ll.next,n,i+1)
    
  def remove(self,ll,n):
    len = self.length(ll)
    if n == len:
      ll = ll.next 
      return ll 
    self.solve(ll,len-n)
    return ll 
 
  
ll = ListNode(1)
ll.next =  ListNode(2)
ll.next.next= ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)

Ans = ListNode().remove(ll,3)
ListNode().traverse(Ans)