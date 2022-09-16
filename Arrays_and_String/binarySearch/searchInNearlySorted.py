


def search(arr, target):
  low=0 
  high= len(arr)-1 
  
  while (low<=high):
    mid = low+(high-low)//2 
    
    if (arr[mid]==target):
      return mid 
    
    
    elif (arr[mid-1]==target and mid>0):
      return mid-1 
    
    
    elif arr[mid+1]==target && mid < len(arr):
      return mid+1 
    
    
    elif (arr[mid]>target):
      high=mid-2
    else :
      low=mid+2
    
    
  
  return -1
