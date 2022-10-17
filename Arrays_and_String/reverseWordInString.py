class Solution:
  def reverseWords(self,str):
    str = list(str)
    n = len(str)
    i=j=0 
    while j<n:
      while j<n and str[j] != " ": j=j+1
      k=j+1
      j=j-1
      while i<j:
        str[i],str[j] = str[j],str[i]
        i=i+1 
        j=j-1
      i=j=k
      
    return "".join(str)
  
  def reverseWords(self,str):
    return " ".join([word[::-1] for word in str.split()])
    
  def reverseWords(self,str):
    res = ""
    for word in str.split():
      word = "".join(reversed(word))
      res += word+" "
    return res 
    
  def reverseWords(self,str):
    stack = [] 
    res = ""
    for char in str:
      if char == " ":
        while stack:
          res +=stack.pop() 
        res +=" "
      else:
        stack.append(char)
    while stack:
      res +=stack.pop()
    return res
 
