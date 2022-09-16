class Solution:
  # find max  
  # reverse 0-> max index 
  # next reverse from 0-> max-1 
  # add index+1, max in result 
  
  def pancakeSort(self,arr):
    
    def reverse(start,end): 
      while start < end:
        arr[start],arr[end] = arr[end],arr[start] 
        start +=1 
        end -=1 
        
    def findMax(end):
      _max = arr[0]
      index = 0 
      for i in range(end):
        if arr[i]>_max:
          index = i 
          _max = arr[i]
      return (index,_max)
      
    result = [] 
    n = len(arr) 
    till = n 
    for i in range(n-1):
      (index,max)= findMax(till)
      reverse(0,index)
      reverse(0,max-1) 
      result.append(index+1) 
      result.append(max) 
      till -= 1 
     
    return result
     
     
 
sort = Solution().pancakeSort
sort([3,2,4,1])