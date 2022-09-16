

class Solution:
  def mergeInBetween(self,list1,a,b,list2):
    
    curr = list1 
    prev = None 
    i = a 
    while i>1:
      curr = curr.next 
      i = i-1 
      
    temp = curr.next
    i = b-a 
    while i >= 0:
      temp=temp.next 
      i=i-1 
    
    curr.next = list2 
    btemp = list2  
    while btemp.next :
      btemp = btemp.next 
    btemp.next = temp
    
    return list1
    
    