# valid parenthesis  

from collections import deque 
class Solution:
  
  def isValid(self,s):
    stack = deque() 
    
    for p in s:
      if p == "(" or p=="{" or p=="[":
        stack.append(p)
      else:
        if not stack:
          return False
        if p == "]" and stack[-1]=="[":
          stack.pop()
      
          
        elif p == ")" and stack[-1]=="(":
          stack.pop()
       
        elif p == "}" and stack[-1]=="{":
          stack.pop()
        else:
          return False 
          
    return not stack 
 
print(Solution().isValid("[]{}()"))