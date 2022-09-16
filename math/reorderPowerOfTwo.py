
class Solution:
    
  def permute(self,str,perms,curr="",i=0):
    if i == len(str):
      if int(curr)&(int(curr)-1)==0:
        perms[1] = True 
      return
    ch = str[i]
    n = len(curr)
    for j in range(n+1):
      left = curr[:j] 
      right = curr[j:n] 
      self.permute(str,perms,left+ch+right,i+1)

  def reorderedPowerOf2(self,n):
    if n==0 or n==10:
      return False 
    if n==1 or n==2:
      return True
    
    if n&(n-1) == 0: return True 
    perms = {} 
    self.permute(str(n),perms,"")
    return True if perms else False
    
    
    
    
res = Solution().reorderedPowerOf2(7373737)
print(res)

