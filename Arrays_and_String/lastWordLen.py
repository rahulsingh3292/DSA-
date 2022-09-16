class Solution:
  def lengthOfLastWord(self,s):
    return len(s.rstrip().split()[-1])
    

print(Solution().lengthOfLastWord("hey how  are youu babby "))