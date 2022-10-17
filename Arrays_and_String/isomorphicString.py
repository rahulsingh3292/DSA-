
# this Q is same as => word pattern 
from collections import OrderedDict
class Solution:
  def isIsomorphic(self,a,b):
    return (list(OrderedDict({char:index for index,char in enumerate(a)}).values()) == list(OrderedDict({char:index for index,char in enumerate(b)}).values()))
    
    