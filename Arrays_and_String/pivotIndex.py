
class Solution:
  def pivotIndex(self,arr):
    n = len(arr)
    k = sum(arr)
    curr = arr[0] 
    if curr == k: return 0
    for i in range(1,n):
      if k-curr-arr[i] == curr:
        return i 
      curr+=arr[i]
    return 0 if k==arr[0] else -1
    
  