class Solution:
  def selectionSort(self, arr):
    for i in range(len(arr)-1):
      for j in range(i+1,len(arr)):
        if arr[j]<=arr[i]:
          arr[i],arr[j] = arr[j],arr[i] 
    