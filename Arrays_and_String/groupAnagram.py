import collections
class Solution:
  def groupAnagrams(self,strings):
    ans = {} 
    for s in strings:
      str = "".join(sorted(s))
      if str not in ans:
        ans[str] = [] 
      ans[str].append(s) 
    return ans.values()
  
  def groupAnagrams(self,strings):
    ans = collections.defaultdict(list)
    for s in strings:
      count=[0]*26 
      for char in s:
        count[ord(char) - ord("a")]+=1 
      
      ans[tuple(count)].append(s)
    return ans.values()
      
 
strs = ["eat","tea","tan","ate","nat","bat"] 


anagram = Solution().groupAnagrams(strs) 
print(anagram)