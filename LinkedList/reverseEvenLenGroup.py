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
  
  def reverseEvenLengthGroups(self ,
  head):
    size = self.length(head)
    temp = head 
    res = None
    updater = res 
    even = False 
    k = 1
    
    while (size>=k) or (size<k and size%2==0 and size>1):
     
      cond = size<k and size%2==0
      if (not even) and (not cond):
        curr = temp
        i = 1 
        while i <= k:
          if res==None:
            res = curr 
            updater = res 
          else:
            updater.next = curr 
            updater = curr
          curr = curr.next
          i = i+1 
        temp = curr
      
     
      if even or cond:
        if size<k:
          k = size
        i = 1
        curr = temp.next
        prev = temp 
        next_updater = prev 
        while i  < k:
          next = curr.next
          curr.next = prev 
          prev = curr 
          curr = next 
          i+=1
        
        updater.next = prev 
        updater = next_updater
        temp = curr 
        
      even = not even
      size -=k
      k+=1 
    
    updater.next = temp 
    return res 
      
          


          
        
      
     
    
head = Node(1) 
head.next = Node(2) 
head.next.next= Node(3)  
head.next.next.next = Node(4)
head.next.next.next.next= Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)


Solution().reverseEvenLengthGroups(head)    
traverse(head)   
    
    
    
    
      
      
    
    
    
    