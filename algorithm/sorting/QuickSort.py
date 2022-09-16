class QuickSort(object):
  def partition(self,arr,left,right):
    
    
    
    mid = left+(right-left)//2
    i,j = left,right 
    pivot = arr[mid]
    
    while i <= j:
      while arr[i] < pivot:
        i +=1 
      while arr[j] > pivot:
        j -=1 
      if i<=j:
        arr[i],arr[j] = arr[j],arr[i] 
        i+=1 
        j-=1
        
    return i-1
    
  def sort(self,arr,left,right):
    if left < right:
      pi = self.partition(arr,left,right)
      self.sort(arr,left,pi) 
      self.sort(arr,pi+1,right) 
      
arr = [1,-1,0]
QuickSort().sort(arr,0,len(arr)-1) 
print(arr)

  
      