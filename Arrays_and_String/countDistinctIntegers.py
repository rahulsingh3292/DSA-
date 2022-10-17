class Solution:
 
    
  def reversedNum(self,n):
    rnum = 0 
    while n:
      digit = n%10 
      rnum = (rnum*10)+digit
      n=n//10 
    return rnum 
    
  def countDistinctIntegers(self,arr):
    res = set(i for i in arr)
    for n in arr:
      res.add(self.reversedNum(n)) 
    return len(res)
    
    
    
 
arr = [2,2,12,21]
res = Solution().countDistinctIntegers(arr)
print(res)
