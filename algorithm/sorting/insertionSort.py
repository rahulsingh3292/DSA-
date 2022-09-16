class Solution:
  def insertionSort(self,arr): 
    # start from 1,n 
    # start inner loop from j=i-1 
    # and loop condition if arr[j] > temp and j>=0 
    # inside inner loop => arr[j+1] = arr[j] 
    # outside loop => arr[j+1] = temp 
    
    n = len(arr)
    i =1
    while i<n:
      temp = arr[i] 
      j = i-1
      while arr[j] > temp and j>=0:
        arr[j+1] = arr[j]
        j-=1 
      arr[j+1] = temp
      i+=1
    return 
 

