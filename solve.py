class Solution:
  def reversedNum(self,n):
    rnum = 0 
    while n:
      digit = n%10 
      rnum = (rnum*10)+digit
      n=n//10 
    return rnum 
    
  def sumOfNumberAndReverse(self,num):
     
    for i in range(int(10e5)+1): 
      r = self.reversedNum(i) 
      if i+r == num: 
        return True 
    return False
     
       
n = 443
print(Solution().sumOfNumberAndReverse(n))
