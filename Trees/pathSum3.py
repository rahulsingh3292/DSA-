
from tree_data import * 

class Solution:
  def __init__(self):
    self.total = 0 
    
  def get(self,root,target,data,curr,total):
    if root is None: 
      return 
    
    curr += root.val 
    if curr-target in data:
      self.total += data[curr-target] 
    if curr in data:
      data[curr] +=1 
    else:
      data[curr] = 1
    self.get(root.left,target,data,curr)
    self.get(root.right,target,data,curr)
    data[curr] -=1 
 
  def pathSum(self,root,target):
    data = {0:1} 
    curr = 0 
    self.get(root,target,data,curr)
    return self.total 