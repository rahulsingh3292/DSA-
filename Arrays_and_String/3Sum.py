class Solution:
  def twoSum(self,arr,current):
    arr.sort() 
    
    n = len(arr) 
    result = set() 
    
    for i in range(n-2):
      j ,k = i+1,n-1 
      
      while i <j:
        a,b,c = arr[i],arr[j],arr[k] 
        ans = a+b+c 
        if ans==0: 
          result.add(ans)
          j+=1 
          k-=1 
          
        elif ans>0: k-=1 
        else: j+=1 
      
          
          
     
  
  