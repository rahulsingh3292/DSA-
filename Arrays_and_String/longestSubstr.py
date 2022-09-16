
class Solution: 
  def lengthOfLongestSubstring(self,str):
    n = len(str)
    i=j=size=0
    data={}
    while j<n:
      char = str[j] 
      if char not in data:
        data[char]=1 
      else:
        data[char]+=1 
      
      window_size = (j-i)+1
      while len(data) < window_size:
          data[str[i]] -=1 
          if data[str[i]] == 0:
            data.pop(str[i])
          i=i+1 
      
      if len(data) == window_size:
        size = max(size,window_size)
      
      j=j+1 
    return size 


