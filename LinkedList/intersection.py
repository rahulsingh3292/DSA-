


# Time Complexity => O(N+M) 
# Space => O(1)
class Solution:
  def getIntersectionNode(self,A,B):
    
    def length(head):
      count=0 
      fast = head 
      while fast and fast.next:
        fast=fast.next.next 
        count+=2 
      return count+1 if fast else count 
 
    
    n,m = length(A),length(B) 
    
    headA = A 
    while n > m:
      headA = headA.next 
      n = n-1 
      
    headB = B 
    while m > n:
      headB = headB.next
      m = m-1 
   
    while headB!=headA and headB:
      headA = headA.next 
      headB=headB.next
      
    return headB 
    
 
# Time Complexity => O(N)  
# Space => O(N) 
class Solution:
  def getIntersectionNode(self,A,B):
    dataA = {} 
    headA = A 
    while headA:
      dataA[headA] = True
      headA = headA.next
    
    headB = B 
    while headB:
      if headA.get(headB):
        return headB
      headB=headB.next 
      
    return None 
    
    
    
        
  
    
    
    
    
    
    
        
  