
from collections import deque 
def interLeaveQueue(arr):
  n = len(arr) 
  # 1 2 3 4 5 6 7 8 9 10
  left = deque() 
  right=deque()
  for i in range(n//2,n):
    right.append(arr[i]) 
    
  for i in range (n//2):
    left.append(arr[i])
  
  i=0 
  while i<n:
    arr[i],arr[i+1] = left.popleft(),right.popleft()
    i=i+2 
  return arr

res = interLeaveQueue([1,2,3,4,5,6,7,8,9,10])
print(res)