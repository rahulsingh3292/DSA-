
class Solution:
  def findMaxAverage(self,arr,k):
    n = len(arr)
    maxAvg=float("-inf")
    currAvg = 0 
    i=j=0 
    while j<n:
      currAvg +=arr[j] 
      if(j-i)+1 == k:
        maxAvg=max(maxAvg,currAvg/k)
        currAvg -=arr[i]
        i=i+1
      j +=1 