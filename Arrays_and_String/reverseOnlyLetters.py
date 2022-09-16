class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s) 
        s = list(s)
        i,j = 0,n-1 
        while i<j:
          a,b = s[i],s[j] 
          if a.isalpha() and b.isalpha():
            s[i],s[j] = b,a 
            i+=1 
            j-=1 
          elif (not a.isalpha()) and (not b.isalpha()):
            j-=1 
            i+=1 
          elif a.isalpha() and (not b.isalpha()):
            j-=1 
          else:
            i+=1 
          
        return  "".join(s) 