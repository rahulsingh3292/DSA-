class ListNode:
  def __init__(self,val=None,next=None):
    self.val = val 
    self.next = next
  
  def reverse(self,head):
    
    curr = head 
    prev = None 
    while curr!=None:
      temp = curr.next 
      curr.next = prev 
      prev = curr
      curr = temp 
      
    return prev
  

    
    
  
    

# 1 -> 2 -> 3 -> 4 
# 4 -> 3 -> 2 -> 1 


ll = ListNode(1)
ll.next = ListNode(2)

ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)


ans = ll.reverse(ll)

def traverse(ll):
  if ll is None:
    return 
  print(ll.val)
  return traverse(ll.next)

traverse(ans)
