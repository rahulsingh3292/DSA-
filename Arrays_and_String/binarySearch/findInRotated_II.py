class Solution: 
  def search(self,arr: list[int], target: int)-> bool :
    
    low = 0 
    high = len(arr)-1 
    while low<= high:
      mid = low+(high-low)//2 
     
      if arr[mid] == target:
        return True 
      
      elif arr[mid]>arr[low]:
        if target<arr[mid] and target>=arr[low]:
          high=mid
        else:
          low=mid+1 
          
      elif arr[mid]<arr[low]:
        if target > arr[mid] and target<arr[low]:
          low=mid+1 
        else:
          high=mid
      else:
        low+=1 
    return False 
 


          
    
    