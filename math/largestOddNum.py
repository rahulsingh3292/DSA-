class Solution:
  def largestOddNumber(self,string):
    n = len(string)
    for i in range(n-1,-1,-1):
      char = string[i]
      if int(char)&1:
        return string[:i+1]
    
  def largestOddNumber(self,string):
    num = int(string) 
    while num:
      digit=num%10 
      if (digit)&1 :
        return str(num)
      num=num//10 
    return ""
  
  
  
res = Solution().largestOddNumber("525")
print(res)
      