import sys 
class Solution:
  def threeSumClosest(self,arr,target):
    arr.sort() 
    n = len(arr)
    closestSum = sys.maxsize 
    for i in range(n-2):
      j,k = i+1,n-1 
      while j<k:
        sum = arr[i]+arr[j]+arr[k] 
        
        if (abs(target-closestSum) > abs(target-sum)): 
          closestSum = sum 
          
        if sum > target:
          k-=1 
        else:
          j+=1 
        
        
          
    return closestSum
          
        
 

arr =  [-1,2,1,-4]
print(Solution().threeSumclosestSum(arr,2))