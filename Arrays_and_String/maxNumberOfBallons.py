
from collections import Counter 
class Solution:
  def maxNumberOfBalloons(self,string):
    target="balloon"
    data = {key:0 for key in target}  
    for char in string:
      if char in data: data[char]+=1 
    mx = 0 
    while True:
      for key in "balon":
        if data[key] <= 0: return mx 
        if (key == "l" or key =="o") and data[key]>=2:
          data[key] -=2 
        elif key =="a" or key=="b" or key=="n":
          data[key] -=1 
        else: return mx
      mx=mx+1 
 
 
string = "balloooonballnajshhshballlonballlooonballloonn"
res = Solution().maxNumberOfBalloons(string)
print(res)