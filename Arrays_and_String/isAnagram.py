from collections import Counter 
class Solution:
  def isAnagram(self, string, target):
    return sorted(string) == sorted(target)
    
  def isAnagram(self,string,target):
    return Counter(string) == Counter(target)
  
  def isAnagram(self,string,target):
    n = len(target) 
    
    if len(string) != n:
      return False 
    
    data = Counter(string) 
    count=len(data)
    for i in range(n):
      char = target[i] 
      if data.get(char) !=  None:
        data[char]-=1 
        if data[char]==0: 
          count-=1 
      else:
        return False 
          
    return count==0 