# maintain variable i=0 and j=1 
# run loop until j < n 
# check if i==0 and j=0  then increment 
# the j pointer..  check for next.. 

# else if i!=0 and j==0 or i!=0 and j!=0
# in this case both pointet ++ .. 

# else if i=0 and j!=0 then swap and increment both pointer ++ 

class Solution: 
  def moveZeros(self,arr):
    
    n = len(arr) 
    i= 0
    j = 1 
    while j<n:
      if arr[i]==0 and  arr[j]==0:
        j+=1 
      
      
      elif (arr[i]!=0 and arr[j]==0) or (arr[i] != arr[j]!=0):
        
         i+=1 
         j+=1
      else:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1 
        j+=1 
    
"""
  i j
# 0,1,0,0,3,2,12 
    
    i j 
# 1,0,0,0,3,2,12 

    i     j 
# 1,0,0,0,3,2,12 
      i     j 
# 1,3,0,0,0,2,12 

        i      j 
# 1,3,2,0,0,0,12
# 1,3,2,12,0,0,0
"""
        

    