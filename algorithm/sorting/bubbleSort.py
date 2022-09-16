class Solution:
  def bubbleSort(self,arr):
    n = len(arr)
    for i in range(n-1):
      is_swapped=False 
      for j in range((n-i)-1):
        if arr[j+1]<arr[j]:
          is_swapped = True 
          arr[j],arr[j+1] = arr[j+1],arr[j]
      if not is_swapped: 
        break
    return arr
 
arr  = [2,3,7,1,0,4,5,7,9,0,1,2,4] 
Solution().bubbleSort(arr) 
print(arr)
