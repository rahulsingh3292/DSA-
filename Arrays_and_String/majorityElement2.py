
from collections import Counter 
class Solution:
  def majorityElement(self,nums):
    n = len(nums)
    return [val for val,count in Counter(nums).items() if count>n//3] 
      