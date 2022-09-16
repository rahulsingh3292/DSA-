def findArraySum(a,n,b,m):
  
  result = [] 
  i= n-1 
  j = m-1 
  carry = 0 
  while i>=0 and j>=0:
    a1,b1 = a[i],b[j]
    ans = a1+b1+carry 
    if ans>9:
      carry=1 
    else:
      carry = 0 
      
    result.append(ans%10)
    
    j-=1 
    i-=1
  
  while i>=0:
    ans = a[i]+carry 
    if ans>9:
      carry = 1 
    else:
      carry = 0 
    result.append(ans%10)
    i-=1 
    
  while j>=0:
    ans = b[j] +carry 
    if ans>9:
      carry = 1 
    else:
      carry = 0 
    result.append(ans%10)
    j-=1 
    
  if carry: result.append(carry)
  result.reverse()
  return result 
