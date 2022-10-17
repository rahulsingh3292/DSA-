class Solution:
  def findMaxK(self,arr):
    data = {arr[i]:i for i in  range(len(arr))}  
    largestNumData = float("-inf")
    for i in range(len(arr)): 
      n = arr[i]
      if -n in data and data[-n] != i :
        largestNumData = max(largestNumData,n) 
    return largestNumData if type(largestNumData) is int else -1
    

arr =[-1,10,6,7,-7,1]
print(Solution().largestNumberExist(arr))