

class ListNode:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 
    
class Solution:
  def mid(self,head):
    slow=fast=head 
    while fast and fast.next:
      fast=fast.next.next 
      slow=slow.next 
    return slow 
  
  # Reversal takes O(1) space 
  def reverse(self,head):
    curr = head 
    prev = None 
    while curr:
      next = curr.next 
      curr.next = prev 
      prev = curr 
      curr=next 
    return prev 
    
  # Time Complexity => O(N)
  # Space => O(1) 
  def pairSum(self,head):
    mid = self.mid(head) 
    rear = self.reverse(mid) 
    maxSum = 0 
    curr = head 
    while curr!=rear and rear:
      rearVal = rear.val 
      frontVal = curr.val 
      maxSum = max(maxSum,frontVal+rearVal)
      rear=rear.next
      curr=curr.next 
    return maxSum 
    
  
  # Time Complexity=> O(N)
  # Space =>  O(N)  stack used..
  def stack(self,head):
    data = []
    curr=head
    while curr:
      data.append(curr.val)
      curr = curr.next 
    return data 
    
  def pairSumStack(self,head):
    mid = self.mid(head) 
    rear = self.stack(mid) 
    maxSum = 0 
    curr = head 
    while curr!= mid and rear:
      rearVal = rear.pop() 
      frontVal = curr.val 
      maxSum = max(maxSum,frontVal+rearVal)
      curr=curr.next 
    return maxSum 
    
    
head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)

sum = Solution().pairSum(head)
print(sum)