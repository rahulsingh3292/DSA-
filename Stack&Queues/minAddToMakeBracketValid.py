class Solution:
  def minAddToMakeValid(self,string): 
    stack = [] 
    count = 0 
    for bracket in string:
      if bracket=="(":
        stack.append("(")
        count +=1 
      else:
        if stack and stack[-1] == "(":
          stack.pop() 
          count -=1 
        else: 
          count +=1 
    return count 
    
    

str = "((()))))))))"
res = Solution().minAddToMakeValid(str)
print(res)
    
    
 
   
    
    
    