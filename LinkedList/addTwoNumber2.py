




# Time Complexity => 0(N) 
# Space => O(1)
class Solution:
  def reverse(self,head):
    curr=head
    prev = None 
    while curr:
      next = curr.next 
      curr.next = prev 
      prev = curr 
      curr=next 
    return prev 
  
  def add(self,list1,list2,carry):
    if list1 and list2:
      sum = list1.val + list2.val + carry 
      carry = 1 if sum > 9 else 0 
      return ListNode(sum%10,self.add(list1.next,list2.next,carry))
    if list1:
      sum = list1.val +carry
      carry = 1 if sum>9 else 0 
      return ListNode(sum%10,self.add(list1.next,list2,carry))
    if list2:
      sum = list2.val +carry
      carry = 1 if sum>9 else 0 
      return ListNode(sum%10,self.add(list1,list2.next,carry)) 
    if carry:
      return ListNode(carry) 
    
  
  def addTwoNumbers(self,list1,list2):
    list1 = self.reverse(list1)
    list2= self.reverse(list2)
    carry = 0 
    return self.reverse(self.add(list1,list2,carry))
    
    
#Time Complexity => O(N)
# Space => O(N)
class Solution:
  def stack(self,head):
    data = list() 
    curr = head 
    while curr:
      data.append(curr.val)
      curr=curr.next 
    return data 
    
  def addTwoNumbers(self,list1,list2):
    A = self.stack(list1)
    B = self.stack(list2)
    node,node_next = None 
    carry = 0 
    res = list()
    while A and B:
      val1 = A.pop()
      val2 = B.pop()
      sum = val1+val2+carry 
      carry = 1 if sum>9 else 0 
      res.append(sum%10) 
      
    while A:
      val = A.pop()
      sum = val+carry 
      carry = 1 if sum>9 else 0 
      res.append(sum%10) 
    
    while B:
      val = B.pop()
      sum = val+carry 
      carry = 1 if sum>9 else 0 
      res.append(sum%10) 
    
    if carry:
      res.append(carry) 
    
    while res:
      num = res.pop() 
      if node is None:
        node = ListNode(num) 
        node_next=node 
      else:
        node_next.next = ListNode(num)
        node_next = node_next.next 
    return node 


    