class Solution:
  def digitSum(self,string,k):
   
    while len(string)>k:
      new = ""
      for i in range(0,len(string)-k,k):

        _sum = sum(map(int,string[i:i+k]))
        new +=str(_sum)
      _sum= sum(map(int,string[i+k:len(string)]))
      new +=str(_sum)
      
      string = new 
    return string
        
  
string = "11111222223"   
print(Solution().digitSum(string,3))