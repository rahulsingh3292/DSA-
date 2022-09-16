class Solution:
  def twoSum(self,arr,target):
    data = {} 
    n = len(arr)
    for i in range(n):
      val = arr[i]
      remain = target-val 
      rIndex = data.get(remain)
      if rIndex!= None and rIndex!=i:
           return i,rIndex
      else:
        data[val] = i 
      

arr = [3,2,4] 
print(Solution().twoSum(arr,6))