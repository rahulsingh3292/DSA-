
class ListNode:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 

def traverse (head):
  if not head:
    return 
  print(head.val,end=" -> ")
  traverse(head.next)
  

def spiralMatrix(head,m,n):
  

class Solution:
  def spiralMatrix(self,m,n,head):
    matrix = [[-1 for j in range(n)] for i in range(m)]
  
    curr = head 
    top,right=0,0
    bottom,left = m-1,n-1 
  
    while curr:
    
      i=right 
      while i <= left and curr:
        matrix[top][i] = curr.val 
        curr=curr.next 
        i+=1
      top +=1 
    
      i = top
      while i<=bottom and curr:
        matrix[i][left] = curr.val 
        curr = curr.next 
        i+=1
      left -=1 
    
    
      i=left
      while i>=right and curr:
        matrix[bottom][i] = curr.val
        i -=1 
        curr= curr.next 
      bottom -=1 
    
      i = bottom 
      while i >= top and curr:
        matrix[i][right] = curr.val
        curr = curr.next 
        i-=1
      right+=1
    
    return matrix 
  
   
    
  
      
    
    
    
      

head = ListNode(3) 
head.next = ListNode(0)
head.next.next = ListNode(2) 
head.next.next.next = ListNode(6) 
head.next.next.next.next = ListNode(8) 
head.next.next.next.next.next = ListNode(1) 
head.next.next.next.next.next.next= ListNode(7) 
head.next.next.next.next.next.next.next= ListNode(9) 
head.next.next.next.next.next.next.next.next= ListNode(4) 
head.next.next.next.next.next.next.next.next.next= ListNode(2) 
head.next.next.next.next.next.next.next.next.next.next= ListNode(5) 
head.next.next.next.next.next.next.next.next.next.next.next= ListNode(5) 
head.next.next.next.next.next.next.next.next.next.next.next.next= ListNode(0) 

spiralMatrix(head,3,5)