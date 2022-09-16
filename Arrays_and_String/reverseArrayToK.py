

class Solution:
  def reverse(self,arr,M):
    i=M+1 
    j = len(arr)-1 
    while i<j:
      arr[i],arr[j]=arr[j],arr[i]
      i+=1 
      j-=1 
      


arr = [1,2,3,4,5,6] 
Solution().reverse(arr,3) 
print(arr)
    