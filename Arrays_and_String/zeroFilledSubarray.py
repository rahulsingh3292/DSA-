
class Solution:
  def zeroFilledSubarray(self,arr):
    total,n= 0,len(arr)
    j=0
    while j<n: 
      while j<n and arr[j]!=0: j=j+1 
      i=j 
      while j<n and arr[j]==0: j=j+1 
      width= j-i
      total +=width*(width+1)//2
    return total
    