
class MergeSort:
  
  def inplaceMerge(self,arr,left,right):
    mid = left+(right-left)//2
    n = mid-left+1
    m = right-mid 
    i=j=0 
    k = left
    a = [arr[left+i] for i in range(n)]
    b = [arr[mid+1+j] for j in range(m)]
   
    while i < n and j<m:
      if a[i] < b[j]:
        arr[k] = a[i]
        i+=1  
      else:
        arr[k] = b[j] 
        j+=1
      k+=1 
    
    while i<n:
      arr[k] = a[i] 
      i+=1 
      k+=1 
      
    while j<m:
      arr[k] = b[j]
      j+=1 
      k+=1 
    
    
  def inplaceSort(self,arr,left,right):
    if left<right:
      mid = left+(right-left)//2 
      self.sort(arr,left,mid) 
      self.sort(arr,mid+1,right) 
      self.merge(arr,left,right)
    return
  
  def mergeArr(self,left,right):
    n,m = len(left),len(right)
    sortedArr = [0]*(n+m)
    i=j=k=0 
    
    while i<n and j<m:
      if left[i] < right[j]:
        sortedArr[k] = left[i] 
        i+=1 
      else:
        sortedArr[k] = right[j] 
        j+=1 
      k+=1 
      
    while i<n:
      sortedArr[k] = left[i] 
      i+=1 
      k+=1 
    while j < m:
      sortedArr[k] = right[j] 
      k+=1 
      j+=1
    return sortedArr 
  
  def sortArr(self,arr):
    if len(arr) == 1:
      return arr 
    mid = len(arr)//2 
    left = self.sortArr(arr[:mid])
    right = self.sortArr(arr[mid:]) 
    return self.mergeArr(left,right)
    
    
arr = [5,3,1,-1,600,-5,0]  
n = len(arr)
arr = MergeSort().sortArr(arr)
print(arr)