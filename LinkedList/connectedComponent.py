
class Node:
  def __init__(self,val,next=None):
    self.val = val 
    self.next = next 


class Solution:
  def numComponents(self,head,nums):
    n = len(nums)
    count=0
    data = {} 
    for k in nums: data[k] = True 
    curr=head
    while curr:
      x = curr.val 
      y,c = None,0
      temp = curr.next 
      while temp and data.get(x) and data.get(temp.val):
        y=temp.val
        data[temp.val] = False 
        temp = temp.next 
        c = c+1 
      curr = temp
      
      if c:
        data[x] = False 
        n=n-c-1
        count+=1
      if n<=1:
        break
    
    for key in data:
      if n<1:
        break 
      if data[key]:
        count+=1 
        n=n-1
    return count 
    
    

head = Node(0)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
head.next.next.next.next.next= Node(5)

nums = [1,2,0,4]
Solution().numComponents(head,nums)

# 0->2->1->4->3 => 0,2,1,4
