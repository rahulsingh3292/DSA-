
class Solution:
  def addSpaces(self,string,spaces):
    res = "" 
    i=0 
    k=0
    while i < len(spaces):
      pos = spaces[i] 
      for j in range(k,pos):
        res +=string[j] 
      k=pos
      res +=" "
      i=i+1
    for i in range(k,len(string)):
      res +=string[i]
    return res 
 
spaces = [0,1,2,3,4,5,6]
str = "spacing" 
res = Solution().addSpaces(str,spaces)
print(res)