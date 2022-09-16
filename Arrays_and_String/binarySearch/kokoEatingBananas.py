import math 


class Solution:
  def isPossible(self, arr: list[int], 
  speed: int, hr: int)-> bool:
    eating_hour: int = 0 
    for n in arr:
      eating_hour+=math.ceil(n/speed) 
    return True if eating_hour<=hr else False 
      
  def minEatingSpeed (self, arr: list[int], hr: int)-> int:
    low: int = 0 
    high: int = max(arr) 
    speed: int = math.inf 
    while low<=high:
      current_speed: = low+(high-low)//2 
      if self.isPossible(arr,current_speed,hr):
        speed = current_speed 
        low=mid+1 
      else:
        high=mid-1  
    return speed 
        
    
    