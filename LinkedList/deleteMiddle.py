class Solution:
  def deleteMiddle(self,head):
    if not head or head.next is None:
      return head 
      
    if head.next.next is None:
      head.next = head.next.next 
      return head
      
    fast = head 
    slow=None 
    while fast and fast.next and fast.next.next:
      fast = fast.next.next
      if slow is None:
        slow = head 
      else:
        slow  = slow.next 
    slow.next = slow.next.next
    return head
  
    

class Node:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 

def traverse (head):
  if not head:
    return 
  print(head.val,end=" -> ")
  traverse(head.next)
  
    
 

ll = Node(1) 
ll.next = Node(3) 
ll.next.next= Node(4)  

ll.next.next.next = Node(7)
ll.next.next.next.next= Node(1)
ll.next.next.next.next.next = Node(2)
ll.next.next.next.next.next.next = Node(6)

ans = Solution().deleteMiddle(ll)
traverse(ans)