
# check if node.next

class ListNode:
  def __init__(self,val=None,
  next=None):
    self.val = val 
    self.next = next
    
  def removeD(self,ll):
    curr = ll 
    sortedList = None 
    prev_Val = None 
    
    while curr is not None:
      if sortedList is None:
        sortedList = ListNode(curr.val)
        prev_Val = curr.val 
        curr = curr.next 
      else:
        if curr.val != prev_Val:
          temp = sortedList
          while temp.next != None:
            temp = temp.next 
          temp.next = ListNode(curr.val)
          prev_Val = curr.val 
          curr = curr.next 
        
        else:
          temp = sortedList 
          # search for distinct value
          prev = curr 
          while prev.next != None and prev.next.val == curr.val:
            prev = prev.next 
         
          
          if temp.next is None:
            if prev.next is None:
              # no such distinct value found.. 
              return 
            
            sortedList = ListNode(prev.next.val) 
            prev_Val = prev.next.val 
            curr = prev.next.next 
            
            
          else:
            while temp.next != None and temp.next.val!=prev_Val:
              temp = temp.next 
            if prev.next is None:
              curr = None
              continue
            
            temp.next = ListNode(prev.next.val) 
            prev_Val = prev.next.val 
            curr = prev.next.next
    return sortedList

class Solution :
  
  def remove(self,ll):
    curr = ll 
    list = None 
    temp = list 
    while curr is not None:
      found = False 
      prev = curr 
      while prev.next!= None and prev.next.val == curr.val:
        found = True 
        prev = prev.next 
        
      if not found:
        if list is None:
          list = ListNode(curr.val)
          temp = list
          curr = curr.next 
        else:
          while temp.next!= None:
            temp = temp.next 
          temp.next = ListNode(curr.val)
          curr = curr.next 
      
      else:
        curr = prev.next
    
    return list 
         
  def recursive(self,ll):
    if ll is not None:
      prev = ll 
      found = False
      while (ll.next != None and ll.next.val == ll.val):
        found = True 
        prev = prev.next 
        ll = ll.next 
      
      if not found:
        return ListNode(ll.val,self.recursive(ll.next))
      else:
        return self.recursive(prev.next)
       
    
    
  def deleteDuplicates (self,ll):
    return self.remove(ll)
        
      

ll = ListNode(1) 
ll.next = ListNode(2)
ll.next.next = ListNode(2)
ll.next.next.next = ListNode(3)

ans = Solution().recursive(ll) 

def traverse(ll):
  if ll is None:
    return 
  print(ll.val)
  traverse(ll.next)
traverse(ans)