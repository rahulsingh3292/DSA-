# leetcode => 1160 
from collections import Counter
class Solution:
  def countCharacters(self,words,chars):
    total = 0
    temp = Counter(chars)
    for word in words:
      counter = Counter(word) 
      found = True 
      for char,count in counter.items():
        if not temp.get(char) or count> temp[char]:
          found=False 
          break 
      if found: total +=len(word)
    return total
