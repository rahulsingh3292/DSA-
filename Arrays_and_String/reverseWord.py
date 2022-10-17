class Solution:
  def reverseWords(self,words):
    words = words.split(" ")
    n = len(words) 
    i = 0
    while i<n:
      if words[i]=="":
        words.pop(i)
        n-=1
      else:
        i+=1 
    words.reverse()
    return  " ".join(words) 
  
  def reverseWord(self,string):
    return " ".join([i for i in reversed(string.split()) if i])
    
  def reverseWord2(self,word):
    word = word.split() 
    n = len(word)
    stack = [] 
    i=0
    while i<n and word[i] == "": i=i+1 
    j=n-1 
    while j>=0 and word[j] == "": j=j-1 
    while i<=j:
      char = word[i]
      if stack and stack[-1] == "" and char=="":
        pass
      else:
        stack.append(char)
      i=i+1
      
    res = "" 
    while stack:
      if len(stack)>1:
        res +=stack.pop()+" "
      else:
        res += stack.pop()
    return res

