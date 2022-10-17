from collections import deque
class Solution:
  def calPoints(self, operations):
    stack= deque() 
    sum = 0 
    for op in operations:
      
      if op=="C":
        
        sum -=int(stack.pop())
      
      elif op=="D":
        val = 2*stack[-1]
        stack.append(val)
        sum +=val
      elif op=="+":
        sum +=sum(stack)
      else:
        stack.append(int(op))
        sum +=int(op)
    return sum 

arr = ["5","2","C","D","+"]
res = Solution().calPoints(arr)
print(res)