class Solution:
  def possible(self,times,current,req_trip):
    total_trips= 0 
    for time in times:
      total_trips+= time//current 
    return total_trips>=req_trip 
  
  def minTime(self,times,trip):
    low = 0 
    high = int(1e12)
    ans = 0 
    while low<= high:
      current = low+(high-low)//2 
      
      if self.possible(times,current,trip):
        ans = current 
        high=mid-1 
      else:
        low=mid+1 
    return ans 