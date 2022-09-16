

class Solution:
  # Iterative Approavch.. 
  def remove(self,ll):
    curr = ll 
    while curr!=None:
      val = curr.val 
      prev = curr 
      while prev.next is not None and prev.next.val == val:
        prev=prev.next 
      
      curr.next = prev.next 
      curr = curr.next 
  
  # Recursive Approach.. 
  def remove(self,ll,prev=None):
    if ll is None:
      return 
    
    if prev != ll.val:
       return ListNode(ll.val,self.remove(ll.next,ll.val))
    else:
      return self.remove(ll.next,prev)
    
  def deleteDuplicates(self,ll):
    return self.remove(ll)
  
 

ll = ListNode(1)
ll.next = ListNode(1)
ll.next.next = ListNode(1)
ll.next.next.next= ListNode(1)
ll.next.next.next.next= ListNode(2)
ll.next.next.next.next.next= ListNode(3)
ll.next.next.next.next.next.next = ListNode(3)

new = ll.deleteDuplicates(ll) 
new.traverse(new)

