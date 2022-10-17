

from collections import deque
class Solution:
  def minRemoveToMakeValid(self,string):
    n = len(string)
    stack  =  deque()
    valid_string = [0]*n 
    for i in range (n):
      char = string[i] 
      if char == "(" or char==")":
        if char=="(":
          stack.append(i) 
        else:
          if stack and string[stack[-1]] == "(":
            valid_string[stack.pop()] = "("
            valid_string[i] = ")"
      else:
        valid_string[i] = char 
    
    return "".join([char for char in valid_string if char!=0])
    
valid_string = "lee(t(c)o(()))))de))))"
print(Solution().minRemoveToMakeValid(valid_string) )       
    
