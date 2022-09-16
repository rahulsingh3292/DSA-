class Node:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 

def traverse (head):
  if not head:
    return 
  print(head.val,end=" -> ")
  traverse(head.next)
  
class Solution:
  def length(self,head):
    fast= head 
    count=0
    while fast and fast.next:
      fast = fast.next.next 
      count+=2
    if fast:
      return count+1 
    return count 
    
  def reverseKGroup (self,head,k):
    if k==1 or (not head.next):
      return head 
    
    size = self.length(head)
    
    temp = head 
    res = temp  
    updater = None
    while size >= k :
      i=1
      curr = temp.next 
      prev = temp 
      next_upater = prev
    
      while i<k:
        next = curr.next 
        curr.next = prev 
        prev = curr 
        curr = next 
        i+=1
      
      
      if res == temp:
        res = prev 
        updater = next_upater
      else:
        updater.next = prev 
        updater = next_upater
 
      temp = curr
      size = size-k 
      
    updater.next = temp 
    head = res 
    return res 
      
  
  
  def reverseKGroup(self,head,k):
    if k == 1:
      return head 
    if head is None:
      return
    group = head 
    last = head 
    i = 1 
    while i < k and last:
      last = last.next 
    
    self.reverse(group,last).next = self.reverseKGroup(last.next)
    return head 
    
  def reverse(self,group,last):
    if not last:
      return group
    curr = group 
    prev = None 
    while curr!=last:
      next = curr.next 
      curr.next=prev
      prev = curr
      curr = next 
    
    return prev 
      
    
    
      
        
      

head = Node(1) 
head.next = Node(2) 
head.next.next= Node(3)  
head.next.next.next = Node(4)
head.next.next.next.next= Node(5)
#head.next.next.next.next.next = Node(6)
ans =      Solution().reverseKGroup(head,3)
traverse(ans)