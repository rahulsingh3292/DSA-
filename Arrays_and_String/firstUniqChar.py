
from collections import Counter
class Solution:
  def firstUniqChar(self,string):
    count = Counter(string)
    for i in range(len(string)):
      if count[string[i]]==1:
        return i 
    return -1 
  
  def firstUniqChar(self,string):
    for i in range(len(string)):
      if string.count(string[i]) == 1:
        return i 
    return -1 
  
  
string = "aabb"
res = Solution().firstUniqChar(string)
print(res)