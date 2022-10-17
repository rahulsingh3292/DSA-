class Solution:
    def runningSum(self,nums):
      n=len(nums)
      res = [0]*n  
      res[0] = nums[0] 
      for i in range(1,n):
        res[i] = res[i-1]+nums[i] 
      return res 