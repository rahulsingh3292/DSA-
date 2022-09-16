class Solution:
  def reverseWords(self,words):
    
    
    words = words.split(" ")
    
    n = len(words) 
   
    i = 0
    while i<n:
     
      if  words[i]=="":
        words.pop(i)
        n-=1 
        
      else:
        i+=1 
      
    
    words.reverse()
   
    return  " ".join(words) 

rev = Solution().reverseWords 
word = "Epg2yl"
print(rev(word))