
def getCount(p,q):
  count=0 
  while p and q:
    bit_p = p&1
    bit_q = q&1 
    if bit_p!=bit_q: count+=1 
    p=p>>1 
    q=q>>1 
  
  while p:
    if p&1: count+=1 
    p = p>>1 
    
  while q:
    if q&1: count+=1
    q = q>>1 
  return count 


