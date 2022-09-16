
def fib(n):
  return n if n<2 else fib(n-1)+fib(n-2)
 

def countZeros(n):
  if not n:
    return 0 
  
  if n%10==0:
    return 1+countZeros(n//10) 
  return countZeros(n//10) 

def findAllIndex(arr,target,n):
  listIndex = [] 
  if n == -1:
     return listIndex

  indexArr=findAllIndex(arr,target,n-1)
  if arr[i]==target:
    indexArr.append(i) 
  return indexArr

def sumArray(arr,i=0):
  if i==len(arr):
    return 0 
  return arr[i]+sumArray(arr,i+1)

def digitSum(n):
  if n == 0:
    return 0 
  return (n%10)+ digitSum(n//10)

print(digitSum(123442-1))