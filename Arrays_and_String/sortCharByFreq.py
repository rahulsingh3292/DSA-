
from collections import Counter 
class Solution:
  def frequencySort(self,string):
    data={} 
    for char in string:
      if data.get(char):
        data[char][0]+=1 
      else:
        data[char] =[1,char]
    sortedFreqData=sorted(data.values())
    return "".join([char*count for count,char in sortedFreqData[::-1]])
   
    
  
  def frequencySort(self,string):
    return "".join([char*count for char,count in Counter(string).most_common()])
    
    
    
str = "tttreeeeew"
res = Solution().frequencySort(str)
print(res)