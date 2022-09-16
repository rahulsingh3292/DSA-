class Solution:
  def duplicateZeros(self,arr):
    n = len(arr) 
    i=0
    while i < n:
      if arr[i] == 0:
        j = n-1 
        while j>i:
          arr[j] = arr[j-1] 
          j-=1 
        arr[i+1] = 0 
        i=i+2
      else:
        i+=1
      
  

class Solution:
  def duplicateZeros(self, arr: List[int]) -> None:
    zeros = arr.count(0)
    i = len(arr) - 1
    j = len(arr) + zeros - 1

    while i < j:
      if j < len(arr):
        arr[j] = arr[i]
      if arr[i] == 0:
        j -= 1
        if j < len(arr):
          arr[j] = arr[i]
      i -= 1
      j -= 1

      
  
