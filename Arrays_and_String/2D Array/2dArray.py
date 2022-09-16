

# inserting row and col wise.. 

import random 

arr = [[0 for i in range(5)] for j in range(3)] 

def insert():
  global arr 
  for row in range(3):
    for col in range(5):
      arr[row][col] = random.randint(0,15)
  

def isPresent(target):
  global arr 
  for row in range(3):
    for col in range(5):
      if arr[row][col] == target: 
        return f"{target} present in at  {row+1} row {col+1} colum"
  return f"{target} not present" 
  
insert() 

# row wise and col wise sum 
def calculate_sum():
  global arr 
  row_sum =  [] 
  for row in range(3):
    sum = 0 
    for col in range(5):
      sum+=arr[row][col] 
    row_sum.append(sum)
  return row_sum

#largest row sum... 
def largest_row_sum():
  global arr 
  ans = [0,0]
  for row in range(3):
    sum = 0 
    for col in range(5):
      sum+=arr[row][col] 
    if sum > ans[1]:
      ans[0]=row+1 
      ans[1]=sum
  return ans 


arr = [[1,2,3],[6,5,3],[9,6,2]] 
for i in range(len(arr)):
  arr[i].sort()
