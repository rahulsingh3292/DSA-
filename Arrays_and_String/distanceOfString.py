class Solution:
  def checkDistances(self,string,distance):
    data = {key:value for key,value in zip([chr(i) for i in range(97,123)],[i for i in range(0,27)])}
    cal ={} 
    for i in range(len(string)):
      str = string[i]
      if str in cal:
        cal[str] = (i-cal[str])-1
        if distance[data[str]] != cal[str]:
          return False 
      else:
        cal[str] = i 
    return True 
    
