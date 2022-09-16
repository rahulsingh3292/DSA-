# Squares of a sorted array 

class Solution:
  def sorted_Square(self,arr,partition,n):
    squareArr = [] 
    left,right =partition,partition+1
    
    while left>=0 and right<n:
      
      if abs(arr[left]) == arr[right]:
        squareArr.append(abs(arr[left]*arr[left]))
        left-=1
      
      elif abs(arr[left])< arr[right]:
        squareArr.append(abs(arr[left]*arr[left]))
        left-=1 
        
      else:
        squareArr.append(abs(arr[right]*arr[right]))
        right+=1 
        
    while right<n:
        squareArr.append(abs(arr[right]*arr[right]))
        right+=1 
        
    while left>=0:
        squareArr.append(abs(arr[left]*arr[left])) 
        left-=1 
        
    return squareArr 
      
      
  def sortedSquares(self,arr):
    n = len(arr)
    partition = 0
    while partition<n and arr[partition] <= 0:
      partition+=1 
    return self.sorted_Square(arr,partitiona-1,n)
    
    
s = Solution().sortedSquares
print(s([-7,-3,2,3,11]))