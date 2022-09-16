class Solution:
  def merge(self,a,m,b,n):
    
   # run while j>=0 and i>=0 
   # if maintain variable i = m-1 
   # j= n-1 and last variable
   # k=(n+m)-1 for 
   # inserting value at in arr1..  
   
   # compare if arr1[i] > arr2[j] then 
   # then insert arr1[i] to arr[k] 
   # and k-- and i-- 
   
   # same with b 
   # over the loop copy remain elemets 
   # at pos arr[k] and poiter --- 
   
   i= m-1 
   j= n-1
   k = (n+m)-1 
   
   while i>=0 and j>=0:
      if a[i] < b[j]:
        a[k] = b[j] 
        k-=1 
        j-=1 
      else:
        a[k] = a[i] 
        i-=1 
        k-=1 
   
      
   while i>=0:
     a[k] = a[i]
     i-=1 
     k-=1 
   while j>=0:
     a[k] = b[j] 
     j-=1 
     k-=1


merge = Solution().merge 
a = [1,3,5,-1,-1,-1,-1] 
b = [0,2,3,4,4]
# 1,2,2,3,6,7
merge(a,3,b,4) 


   
     
          