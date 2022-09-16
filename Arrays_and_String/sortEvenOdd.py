class Solution:
  def sort(self,arr,n,is_ascending=True):
    step = 2
    start = 0 if is_ascending else 1 
    for i in range(start,n-1,step):
      for j in range(i+2,n,step):
        a,b = arr[i],arr[j] 
        if is_ascending:
          if a>b:
            arr[i],arr[j] = arr[j],arr[i]
        else:
          if a < b:
            arr[i],arr[j] = arr[j],arr[i]
    
  
  def sortEvenOdd(self,arr):
    n = len(arr) 
    self.sort(arr,n)
    self.sort(arr,n,False)
    return arr
  

sort = Solution().sortEvenOdd 

arr = [9,6,4,1,2,39,6] 
sort(arr) 
print(arr)

  
  