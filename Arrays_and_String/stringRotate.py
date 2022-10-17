class Solution:
  def rotateString(self,a,b):
    a,b=list(a),list(b)
    if a == b: return True 
    n = len(a) 
    for i in range(n):
      a.append(a.pop(0)) 
      if a==b: return True 
    return  False 