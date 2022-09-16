import random 

arr = [[0 for i in range(4)] for j in range(3)] 

def insert():
  global arr 
  for row in range(3):
    for col in range(4):
      arr[row][col] = random.randint(0,15)
      
def wavePrints(arr,r,c):
  ans = [] 
  for col in range(c):
    if col%2==0:
      for up in range(r):
        ans.append(arr[up][col])
    else:
      for down in range(r-1,-1,-1):
        ans.append(arr[down][col])
  