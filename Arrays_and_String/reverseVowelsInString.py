
class Solution:
  def reverseVowels(self,string):
    vowels = {"a":1,"e":1,"i":1,"o":1,"u":1,"A":1,"E":1,"I":1,"O":1,"U":1}
    string = [char for char in string]
    n=len(string)
    i=0 
    j=n-1 
    while i<j:
      x,y = string[i],string[j] 
      if vowels.get(x) and vowels.get(y):
        string[i],string[j] = string[j],string[i]
        i=i+1  
        j=j-1 
      elif not vowels.get(x) and not vowels.get(y):
        i=i+1 
        j=j-1 
        
      elif not vowels.get(x):
        i=i+1 
      else:
        j=j-1 
    return "".join(string)

str = "hello"
print(Solution().reverse(str))