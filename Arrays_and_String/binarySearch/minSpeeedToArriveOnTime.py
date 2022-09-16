from math  import ceil 

class Solution:
  def checkSpeeed(self,speed,distance,hour,length):
    ans = 0.0
    for i in range(length-1):
      ans+= ceil(distance[i]/(speed)
    ans+= distance[-1]/(speed) 
    return ans<=hour 
    
  def minSpeed(self,distance,hour):
    low = 1
    high = int(1e7)+5
    ans = -1 
    length = len(distance)
    while low<= high:
      speed = low+(high-low)//2 
      if self.checkSpeeed(speed,distance,hour,length):
        ans = speed 
        high = speed-1 
      else:
        low = speed+1 
    return ans
    
    
  