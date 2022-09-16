from collections import Counter 

class Solution:
  def canConstruct(self,ransomNote,magazine):
    
    magazine = Counter(magazine) 
    ransomNote = Counter(ransomNote)
  
    for char in ransomNote :
      if not magazine[char]:
        return False 
        
      if ransomNote[char] > magazine[char]:
        return False 
        
    return True 
    
    