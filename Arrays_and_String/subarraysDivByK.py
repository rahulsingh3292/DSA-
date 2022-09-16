class Solution:
  def subarraysDivByK(self,arr,k):
    map = {0:1} 
    total=sum=0
    for n in arr:
      sum +=n 
      remainder = sum%k 
      if remainder in map:
        total+=map[remainder]
      map[remainder] = 1 if remainder not in map else map[remainder]+1
    return total 
    
    
    