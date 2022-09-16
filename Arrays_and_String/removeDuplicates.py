class Solutlefton:
  def removeDuplicates(self,arr):
    
    n = len(arr)
    left,right=0,1 
    
    while right < n:
      
      if arr[left] == arr[right]: 
        current = arr[right]
        while (right+1<n) and (arr[right+1] == current):
          n-=1 
          arr.pop(right+1) 
        
        left+=1 
        right+=1
          
      else:
        left+=1 
        right+=1
  
  def removeDuplicates(self,arr):
    n = len(arr)
    i = 0 
    for n in arr:
      if (i==0 or i==1) or n!=arr[i-2]:
        arr[i] = n 
        i+=1 
    
        
  
      
        
    
     
  
       
         
        
       
         

remove = Solutlefton().removeDuplicates 
arr = [0,0,2,2,2,2,2,2,2,2,2,2,3,4,4]
remove(arr)

      