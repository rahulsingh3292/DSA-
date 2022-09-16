class countSort:
  def sort(self,arr):
    max_element = max(arr) 
    min_element = int(min(arr))
    n = len(arr)
    range_element = max_element-min_element +1 
    count = (range_element)*[0] 
   
    for i in range(n):
      count[arr[i]- min_element]+=1 
    
    for i in range(1,len(count)):
      count[i]+= count[i-1]
      
    output = [0]*n
    j = n-1 
    while j>=0:
      output[count[arr[j]- min_element] -1] = arr[j] 
      count[arr[j]-min_element]-=1
      j-=1
      
    for i in range(n):
      arr[i] = output[i]
    return arr 
    


arr = [4,-1] 
countSort().sort(arr)
print(arr)
      
    