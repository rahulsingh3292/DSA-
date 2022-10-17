
class Solution:
  def longestContinuousSubstring(self,string):
    n=len(string)
    if n==1: return 1 
    size = 0
    prev=ord(string[0])
    i=0
    for j in range(1,n):
      current = ord(string[j])
      if current-prev==1:
        prev = current
      else:
        size = max(size,j-i)
        i=j
        prev = current
    return max(size,(j-i)+1)

string = "abcdef"
print(Solution().longestContinuousSubstring(string))
   