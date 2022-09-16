class Solution:
  
  # Iterative Approach.. 
  
  def mergeTwoLists(self,l1,l2):
    if (l1 is None) or (l2 is None):
      return l1 or l2 
    
    res=temp=None 
    while l1!=None and l2!=None:
      if l1.val < l2.val:
        if res is None:
          res=ListNode(l1.val) 
          temp = res 
        else:
          while temp.next !=None:
            temp = temp.next 
          temp.next = ListNode(l1.val)
        l1=l1.next 
      else:
        if res is None:
          res=ListNode(l2.val) 
          temp = res 
        else:
          while temp.next !=None:
            temp = temp.next 
          temp.next = ListNode(l2.val)
        l2 = l2.next 
    
    while l1 is not None:
      while temp.next !=None:
        temp = temp.next 
      
      temp.next = ListNode(l1.val)
      l1=l1.next 
    
    while l2 is not None:
      while temp.next != None:
        temp = temp.next 
      temp.next = ListNode(l2.val)
      l2=l2.next 
    
    return res 
 
  # Recustive approach.. 
  def merge(self,l1,l2):
    if (l1 is not None) and (l2 is not None):
      
      if l1.val < l2.val:
        return ListNode(l1.val,self.merge(l1.next,l2))
      else:
        return ListNode(l2.val,self.merge(l1,l2.next))
    
    if l1 is not None:
      return ListNode(l1.val,self.merge(l1.next,l2)) 
    if l2 is not None:
      return ListNode(l2.val,self.merge(l1,l2.next))
  
      
  def mergeTwoLists(self,l1,l2):
    return self.merge(l1,l2)
    