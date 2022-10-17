class Solution:
  
  def reverseString(self,string):
    # two pointers algorithm => O(1) space
    n=len(string)
    i,j=0,n-1 
    while i<j:
      string[i],string[j]=string[j],string[i] 
      i=i+1 
      j=j-1 
      
  def reverseString(self,string):
     # built in arr.reverse() => O(1) space=>  in-place reverse 
     
     # built in reversed(iterative) => O(n)=> space returning new array
     string = reversed(string)
  
  def reverseString(self,string):
    # slicing => O(n) space
    string = string[::-1]
    
  def reverseString(self,string):
    # list comprehension => O(n) space
     string = [string[i] for i in range (len(string)-1,-1,-1)]
     
  def reverseString(self,string):
    # using stack => O(n) space 
    newStr = []
    while string:
      newStr.appene(string.pop())
    string = newStr
  
  def reverseString(self,string):
    i=0 
    while i<len(string)//2:
      string[i],string[n-i-1] = string[n-i-1],string[i]
  
    