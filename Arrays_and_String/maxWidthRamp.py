
class Solution:
  def maxWidthRamp(self,arr):
    n = len(arr)
    left = []
    left.append(0)
    for i in range(1,n):
      if arr[left[-1]] > arr[i]:
        left.append(i)
      else:
        left.append(left[i-1])
    
    right = [-1]*n
    right[-1] = n-1
    for i in range (n-2,-1,-1):
      if arr[i] > arr[right[i+1]]:
        right[i] = i 
      else:
        right[i] = right[i+1]
 
    mx=i=j=0
    while i<n and j<n:
      if arr[right[j]] >= arr[left[i]]:
        mx = max(mx,right[j]-left[i])
        j=j+1
      else:
        while i<n and arr[left[i]] > arr[right[j]]:
          i=i+1
    return mx 
    
arr = [9,8,1,0,1,9,4,0,4,1]
print(Solution().maxWidthRamp(arr))