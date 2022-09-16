class Solution:
  def compareVersions(self,v1,v2):
    v1 = v1.split(".")
    v2 = v2.split(".")
    
    if int(v1[0]) > int(v2[0]): 
      return 1 
      
    if int(v1[0]) < int(v2[0]):
      return -1 
      
    n,m = len(v1), len(v2)
    i=j=0 

    while i < n and j<m:
      a ,b = v1[i],v2[j] 
      if int(a) == int(b):
        i+=1 
        j+=1 
        
      elif int(a) < int(b):
        return -1 
      else:
        return 1 
    
    v1sum = 0 
    v2sum = 0 
    while i<n:
      v1sum += int(v1[i])
      i+=1 
    while j<m:
      v2sum+= int(v2[j])
      j+1 
    
    if v1sum==v2sum:
      return 0 
    elif v1sum>v2sum:
      return 1 
    else:
      return  -1 
        
    
      