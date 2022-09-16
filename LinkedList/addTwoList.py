class Solution:
  
  def addTwoNumbers(self,l1,l2):
    temp = res = None 
    carry = 0 
    while l1 != None and l2!=None:
      if res is None: 
        add = l1.val + l2.val 
        node = ListNode(add%10)
        if add > 9: carry=1 
        res = node 
        temp = res 
        del node
      else:
        while temp.next != None:
          temp = temp.next 
        add = l1.val+l2.val + carry
        carry = 1 if add>9 else 0 
        temp.next = ListNode(add%10)
  
      l1 = l1.next 
      l2=l2.next 
    
    while (l1 is not None):
      add = l1.val+carry 
      carry = 1 if add>9 else 0 
     
      while temp.next != None:
        temp = temp.next 
      
      temp.next = ListNode(add%10)
      l1 = l1.next 
    
    while (l2 is not None):
      add = l2.val+carry 
      carry = 1 if add>9 else 0 
      if temp.next != None:
        temp = temp.next 
      temp.next = ListNode(add%10)
      l2 = l2.next
      
    if carry:
      while temp.next != None:
        temp = temp.next
      temp.next = ListNode(carry)
    return res
  
  def add(self,l1,l2,carry=0):
    if (l1 is not None) and (l2 is not None):
      sum = l1.val+ l2.val + carry
      carry = 1 if sum>9 else 0 
      return ListNode(sum%10,self.add(l1.next,l2.next,carry)) 
    else:
      if l1 is not None: 
        sum = l1.val+carry
        print(sum)
        carry = 1 if sum>9 else 0
        return ListNode(sum%10,self.add(l1.next,l2,carry))
        
      if l2 is not None: 
        sum = l2.val+carry 
        print(sum)
        carry = 1 if sum>9 else 0
        return ListNode(sum%10,self.add(l1,l2.next,carry))
     
      if carry:
          return ListNode(carry) 
  
        
  def addTwoNumbers(self,l1,l2):
    return self.add(l1,l2,0)
     
l1 = ListNode(2)  
l1.next = ListNode(4)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
 
l2 = ListNode(5)
l2.next = ListNode(9)

ans = ListNode().add(l1,l2) 
print(ans.traverse(ans))
      
        
          