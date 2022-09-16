class inPlaceSort:
 
  def reverseArray(self,arr):
    n = len(arr) 
    _arr = [0]*n 
    
    for i in range(n):
      _arr[i] = arr[n-i-1] 
    
    return _arr 
  
  def reverseArray(self,arr):
    n = len(arr)
    for i in range(n//2):
      arr[i],arr[n-i-1] = arr[n-1-i],arr[i]
    return arr
  

print(inPlaceSort().reverseArray([1,2,3,4,5,5]))