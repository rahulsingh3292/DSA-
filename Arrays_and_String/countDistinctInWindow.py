
# problem => count distinct element in every Window of size k 
class Solution:
  def countDistinct(self,arr,k):
    counter = {} 
    i=j=0 
    res = [] 
    while j <len(arr):
      val = arr[j] 
      if val in counter:
        counter[val] +=1 
      else:
        counter[val] = 1 
      
      if j-i+1==k:
        res.append(len(counter)) 
        if counter[arr[i]] == 1:
          counter.pop(arr[i]) 
        else:
          counter[arr[i]] -=1 
        i +=1 
      j +=1 
    return res   
    