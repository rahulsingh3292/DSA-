
class Solution:
  def multiply(self,a,b):
    p,x = 1,0
    for i in range(len(a)-1,-1,-1):
      x = ((ord(a[i])-ord("0"))*p)+x 
      p*=10 
    
    p,y= 1,0
    for i in range(len(b)-1,-1,-1):
      y=((ord(b[i])-ord("0")*p)+y
      p*=10 
    return str(x*y)
    
    
Solution().product("123","52")