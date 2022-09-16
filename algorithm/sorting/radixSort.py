class CountSort(object):
  def sort(self,arr,place):
    max_element = (max(arr)//place)
    n = len(arr)
    output = [0]*n 
    count = [0]*(max_element+1) 
    
    for i in range(n):
      val = arr[i]//place 
      count[(val%10)]+=1 
    
    for i in range(1,len(count)):
      count[i] +=count[i-1] 
      
    i = n-1 
    while i>=0:
      val = arr[i]//place 
      output[count[(val%10)]-1] = arr[i] 
      count[(val%10)]-=1
      i-=1 
    
    for i in range(n):
      arr[i] = output[i] 
    
countSort = CountSort().sort 


class RadixSort:
  def sort(self,arr):
    max_element = max(arr)
    place = 1
    while max_element//place>0:
      countSort(arr,place)
      
      place*=10 
    
      
data = [5,4,2,1,700,8000,2,0,7]
RadixSort().sort(data) 
print(data)