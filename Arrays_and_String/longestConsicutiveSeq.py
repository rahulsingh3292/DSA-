
class Solution:
  def longestConsicutiveSeq(self,arr):
    n = len(arr)
    map = {key:1 for key in arr} 
    mp = map.copy()
    mx = 0
    for key in mp:
      if not map: break
      if key not in map:
        continue 
      count = 0 
      js,jb = key-1,key+1
      while map.get(js) is not None:
        count +=1 
        map.pop(js)
        js = js-1 
        
      while map.get(jb) is not None:
        count +=1 
        map.pop(jb)
        jb = jb+1
      
      map.pop(key)
      mx = max(mx,count+1)
    return mx 
    
  
   
   
   
   
    
    
    
 
arr = [0,3,2]
Solution().longestConsicutiveSeq(arr)

