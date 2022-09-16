import collections 
class Solution:
  def countAnagram(self,string,target):
    # Time Limit will exceed...  
    n = len(target)
    target = sorted(target)
    result = list() 
    for i in range(len(string)):
      word = sorted(string[i:i+n])
      if word == target:
        result.append(i)
    return result 
  
  # using Sliding window.. 
  def findAnagrams(self,string,target):
    n = len(string)
    k = len(target)
    data = collections.Counter(target) 
    count = len(data)
    result = list()
    i=j=0 
    while j<n:
      if data.get(string[j]) != None:
        data[string[j]]-=1 
        if data[string[j]] == 0:
          count-=1 
        
      if (j-i)+1<k:
        j+=1 
      else:
        if count == 0:
          result.append(i)
        
        if data.get(string[i])!=None:
          data[string[i]]+=1 
          if data[string[i]]==1:
            count+=1 
        i+=1 
        j+=1 
          
    return result 
    
    
   
  def search(self,pat,txt):
    return self.countAnagram(txt,pat)

string = "forxxorfxdofrordfororforforfforroffor"

print(Solution().countOccurenceOfAnagram(string,"for"))
    
      
        
    
    
    