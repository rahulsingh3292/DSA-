class Solution:
  def check(self,string):
    n = len(string)
    i=0 
    aFound = False 
    while i<n and string [i]="a":
      aFound=True 
      i+=1 
    j = i+1 
    while j<n:
      if string[j]=="a":
        return False 
      j+=1 
    return True if (not aFound) else True
    