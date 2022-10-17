class Solution:
  def shuffleArray(self,arr,n):
    
    i,res=0,list()
    for j in range(n,len(arr)):
      res.append(arr[i])
      res.append(arr[j])
      i=i+1 
    return res 
  
arr,n=[2,5,1,3,4,7], 3 
res = Solution().shuffleArray(arr,n)
print(list(res))
"""
  2,5,1,3,4,7 n=3 
  2,3,5,4,1,7 
"""