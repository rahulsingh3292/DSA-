class Solution:
  
  def fourSum(self,arr,target):
    arr.sort()
    n = len(arr) 
    result = set() 
    for i in range(n-2):
      for j in range(i+1,n-1):
        a,b = arr[i],arr[j] 
        remain =target-(a+b)
        
        left=j+1 
        right = n-1 
        while left<right:
          c,d = arr[left],arr[right] 
          _sum = c+d 
          if _sum == remain:
            result.add((a,b,c,d)) 
            left+=1 
            right-=1 
            while left<right and arr[left-1] == arr[left]:
              left+=1 
            while right>left and arr[right] == arr[right+1]:
              
              right-=1 
            
          elif _sum > remain:
            right-=1 
          else:
            left+=1 
    return result
    