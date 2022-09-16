

class ListNode:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 

def traverse (head):
  if not head:
    return 
  print(head.val,end=" -> ")
  traverse(head.next) 
 
class Solution:
  def sortList(self,head):
    if not head or  not head.next:
      return head 
    zeros=zeros_next = None 
    ones=ones_next = None 
    twos=twos_next = None 
    curr = head 
    while curr:
      val = curr.data
      if val == 0:
        if zeros is None:
          zeros = curr 
          zeros_next=zeros 
        else:
          zeros_next.next = curr 
          zeros_next = zeros_next.next 
      elif val == 1:
        if ones is None:
          ones = curr 
          ones_next = ones 
        else:
          ones_next.next = curr 
          ones_next=ones_next.next 
          
      else:
        if twos is None:
          twos=curr 
          twos_next = twos 
        else:
          twos_next.next = curr 
          twos_next=twos_next.next 
      
      curr = curr.next
      
    if zeros:
      zeros_next.next = ones 
    if ones:
      ones_next.next = twos 
    if twos:
      twos_next.next = curr 
    
    return zeros if zeros else ones
  
 
ll = ListNode(2) 
ll.next = ListNode(0)
ll.next.next = ListNode(2) 
ll.next.next.next = ListNode(2) 
ll.next.next.next.next = ListNode(1) 
ll.next.next.next.next.next = ListNode(0) 
ll.next.next.next.next.next.next= ListNode(1) 
ll.next.next.next.next.next.next.next= ListNode(0) 

res = Solution().sortList(ll)
traverse(res)