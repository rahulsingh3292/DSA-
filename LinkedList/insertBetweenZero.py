

class Node:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 

class Solution:
  def mergeNodes(self,head):
    temp = Node(-1) 
    temp_next=temp 
    curr=head.next 
    sum = 0 
    while curr:
      wasZero = False 
      if curr.val == 0:
        temp_next.next = curr 
        curr.val = sum
        temp_next=temp_next.next
        sum = 0 
        wasZero=True 
       
      if not wasZero:
        sum = sum+curr.val 
      curr=curr.next 
    
    return temp.next
    
head = Node(0)  
head.next = Node(3)  
head.next.next = Node(1)  
head.next.next.next = Node(0)  
head.next.next.next.next = Node(4)  
head.next.next.next.next.next = Node(5) 
head.next.next.next.next.next.next = Node(2)  
head.next.next.next.next.next.next.next = Node(0)  

Solution().mergeNodes(head)