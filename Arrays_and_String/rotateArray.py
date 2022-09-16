class Solutstarton:
  def reverse(self,arr,start,end):
    while start<end:
      arr[start],arr[end] = arr[end],arr[start] 
      end -=1 
      start +=1 
      
  def rotate(self,arr,k):
    n = len(arr)
    if  k==n: return 
    
    if k>n:
      k=k%n 
    
    self.reverse(arr,(n)-k,n-1)
    self.reverse(arr,0,(n)-k-1)
    self.reverse(arr,0,n-1)

 
1,2,3,4,6,5 
4,3,2,1,6,5 
5,6,1,2,3,4 

    