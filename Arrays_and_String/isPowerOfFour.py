class Solution:
  def isPow(self,n: int ,b: int=16)-> bool:
    if not b:
      return 1 
    ans: int = 4*self.isPow(n,b-1)
    if ans==n: return 1 
    if ans > n: return 0 
    return ans 
    
  def isPowerOfFour (self,n: int)-> bool:
    if n<=0:
      return False 
    if n==1:
      return True 
      
    return self.isPow(n) 
 


  
  