class Solution:
  
  def length(self,head):
    if head is None:
      return 0 
    return 1+self.length(head.next)
  
  def rotateRight(self,head,k):
    if not head or k==0 or head.next is None:
      return head 
      
    len = self.length(head)
    if k > len: k= k%len
    if k==len or k ==0: return head 
    
    curr = head 
    i = 1 
    while i < (len-k):
      curr = curr.next 
      i+=1 
    
    rotatedList = curr.next 
    curr.next = None 
    frontNext = head
    head = rotatedList
    temp = head
    while temp.next is not  None:
      temp = temp.next
    temp.next = frontNext
    return head 
    
    
    


ll = ListNode(1) 
ll.next = ListNode(2)
ll.next.next = ListNode(3) 
ll.next.next.next = ListNode(4) 
ll.next.next.next.next = ListNode(5) 

list = ll.rotate(ll,10)
print(list.val)
     
    
  
# 1,2,3,4,5 
# 4,5,1,2,3