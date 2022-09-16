class Solution:
 
  def solve(self,ll,org):
    if ll is  None:
      return org 
    
    val = ll.val 
    node = self.solve(ll.next,org)
    if (node is False) or (node.val != val):
      return False
    
    if node.next is None:
      return True
    return node.next
  
  def isPalindrome(self,ll):
    return self.solve(ll,ll)
    
  # using Slow fast pointer 
  def isPalindrome(self,head):
    
    slow=fast=head
    while fast and fast.next:
      fast = fast.next.next 
      slow = slow.next 
    
   
    curr = slow
    prev = None
    while curr: 
      next = curr.next 
      curr.next = prev 
      prev = curr
      curr = next 
    fast = prev 
    while fast:
      if fast.val != head.val:
        return False 
      fast=fast.next
      head = head.next
    return True
    
    
      
    
    
class  ListNode:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 
    
    #5 -> 2 -> 5 -> 2 -> 3
    # 5   2    3    2     5 
ll = ListNode(5)
ll.next= ListNode(2)
#ll.next.next.next = ListNode(5)
print(Solution().isPalindrome(ll))