
from collections import OrderedDict
class Solution:
  def kthDistinct(self,arr,k):
    data = OrderedDict() 
    for char in arr:
      if char in data:
        data[char] +=1 
      else:
        data[char] = 1 
    
    distinct = [char for char,count in data if count==1]
    return "" if k>len(distinct) or not distinct else distinct[k-1]
   