

class ListNode:
  def __init__(self,val=None,next=None):
    self.val = val 
    self.next = next 
    
def traverse(head):
  if not head:
    return 
  print(head.val,end="->")
  traverse(head.next)
  
class Solution:
  def merge(self,A,B):
    
    headA = A 
    headB = B 
    temp= ListNode(-1)
    temp_next=temp
    while headA and headB:
      if headA.val < headB.val:
        temp_next.next = headA
        temp_next= headA
        headA = headA.next 
        
      else:
        temp_next.next = headB
        temp_next=headB 
        headB=headB.next 
    
    while headA:
      temp_next.next = headA
      temp_next=headA
      headA=headA.next 
    
    while headB:
      temp_next.next = headB
      temp_next=headB
      headB=headB.next
    
    return temp.next
    
  def mid(self,head):
    slow=head 
    fast = head.next
    while fast and fast.next:
      fast=fast.next.next 
      slow = slow.next 
    return slow 
    
    
  def sort(self,head):
    if not head or not head.next:
      return head 
    
    mid = self.mid(head)
    l = head 
    r = mid.next 
    mid.next = None 
    left = self.sort(l)
    right= self.sort(r)
    return self.merge(left,right)
  
  def sortList(self,head):
    return self.sort(head)
class Solution:
  def sortList(self,head):
    return Sort().sort(head)
    
head = ListNode(1) 
head.next = ListNode(5) 
head.next.next = ListNode(8) 
head.next.next.next= ListNode(4) 
head.next.next.next.next= ListNode(4) 
head.next.next.next.next.next= ListNode(-1) 

ans = Sort().sort(head)
traverse(ans)