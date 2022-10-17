
class Solution:
  def sortPeople(self,names,heights):
    res = sorted(zip(heights,names)) 
    return [res[i][1] for i in range(len(res)-1,-1,-1)]
 
names = ["Alice","Bob","Bob"]
heights = [155,185,150]
print(Solution().sortPeople(names,heights))
 