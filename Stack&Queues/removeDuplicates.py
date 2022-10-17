class Solution:
  def removeDuplicates(self,string):
    stack = [] 
    for s in string:
      if stack and stack[-1]==s:
        stack.pop() 
      else: stack.append(s) 
    return "".join(stack) 
  
 
      

res = Solution().remove("azxxzy") 
print(res)