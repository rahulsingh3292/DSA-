class Solution:
  def findKthPositive(self,arr):
    n = len(arr)
    i = 0  
    res=[]
    for j in range(1,2001):
      if i<n and arr[i] != j:
        res.append(j) 
      else:
        if i >= n:
          res.append(j)
        else:  i=i+1 
    return res[k-1] 


  
