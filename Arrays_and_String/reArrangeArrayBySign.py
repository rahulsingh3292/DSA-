
from collections import deque
class Solution:
  def reArrangeBySign(self,arr):
    positive = deque([n for n in arr if n>=0])
    negative = deque([n for n in arr if n<0])
    res = []
    while positive or negative:
      res.append(positive.popleft())
      res.append(negative.popleft()) 
    return res 
    
  
  def reArrangeArr(self,arr):
    n = len(arr)
    res = [0]*n  
    posIdx,negIdx=0,1
    for val in arr: 
      if posIdx>=n or negIdx>=n: break 
      if val>=0:
        res[posIdx] = val 
        posIdx+=2 
      else:
        res[negIdx] = val 
        negIdx +=2 
    return res 

