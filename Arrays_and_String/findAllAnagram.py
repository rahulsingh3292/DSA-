
from collections import Counter 
class Solution:
  def findAnagram(self,string,target):
    
    k = len(target)
    data = Counter(target) 
    result=list()
    count = len(data)  # total distinct count of target 
    n = len(string)
    i=j=total=0 
    
    while j<n:
      char = string[j]
      """
      check if char in map. then decrease it count by 1 . and when count of this char hit to 0 then decrease count variable also by 1 .. 
      """
      if data.get(char) != None:
        data[char] -=1 
        if data[char]==0:
          count -=1 
          
      if(j-i)+1 == k:
        """
        we reached to our target length.. now we need to check if all the target char count is 0 in map then the our count variable will also be zero..
         now it means anagram find..
         
        after that check if the iTH char present in map or not.. 
        
        if its present in map. then increase map of iTH char by 1 and then 
        
        check if the iTH char count is 1 then increase count var by 1 .. for next time 
        """
        if count==0:
          result.append(i)
          
        if data.get(string[i]) != None:
          data[string[i]]+=1 
          if data[string[i]] == 1:
            count+=1 
            
        i=i+1 
      j=j+1 
    
    return result 

string ="forrofforxyfor"
target="for"
res = Solution().findAnagram(string,target)
print(res)