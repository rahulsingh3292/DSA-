
from collections import deque
class Solution:
  def remove(self,string):
    stack = deque() 
    for char in string:
      if char == "*":
        stack.pop() 
      else:
        stack.append(char) 
    return "".join(stack)

print(Solution().remove("leet**cod*e"))
