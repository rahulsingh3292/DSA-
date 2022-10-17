

class Solution:
  def smallestEvenMultiple(self,n):
    if not n%2: return n 
    for i in range(n,(150*n)+1,n):
      if i%2==0:
        return i 
 
res = Solution().smallestEvenMultiple(150)
print(res)