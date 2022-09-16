class Solution:
  def check(self,x,b=20):
    if not b:
      return 1 
    
    ans = 3*self.check(x,b-1)
    if ans is False or ans > x:
      return False
    
    if ans==x:
      return True 
    return ans 
    
  def isPowerOfThree(self,x):
    if x <= 0 :
      return False 
    if x == 1:
      return True 
    
    tmp = x 
    while tmp > 1:
      tmp//=3 
    print(tmp)

Solution().isPowerOfThree(26)