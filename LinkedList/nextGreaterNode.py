
    
from collections import deque 
class Solution:
  def toList(self,head):
    curr = head 
    list = []
    length = 0 
    while curr:
      length+=1 
      list.append(curr)
      curr=curr.next 
    return (list,length)
    
  def nextLargerNodes(self,head):
    stack = deque() 
    (nodes,n)= self.toList(head) 
    res =[0]*(n)
    n=n-1 
    stack.append(nodes.pop())
    for i in range(n-1,-1,-1):
      node = nodes[i]
      if stack and stack[-1].val > node.val:
        res[i] = stack[-1].val
        stack.append(node) 
      else:
        while stack and stack[-1].val<=node.val:
          stack.pop() 
        
        if stack:
          res[i] = stack[-1].val 
        stack.append(node)
    return res 
  