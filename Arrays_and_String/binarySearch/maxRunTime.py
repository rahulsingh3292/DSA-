# maximum running time of N Computer.. 

# 1. firts check if it's possible to run all computers with given minute at the same time..

# 2. sort the array and check from right side

# 3. and run the loop untill battries[time]>=minute 
# if battries[time] remained then sum all the battries[time].. 

# 4. and check if sum(battries[time])//current_minute>=n .. 

# 5. if it's possible then check for next minute... 


class Solution: 
  def possible(self,battries,minute,n):
    i = len(arr)-1 
    while battries[i]>=minute and i>=0:
      computer+=1 
      i-=1 
    if computer+((sum(battries[:i+1]))//minute)>=n: 
      return True
    return False 
    
  def maxRunTime(self,n,battries):
    battries.sort() 
    low  = battries[0]
    high= int(1e32)
    ans = 1 
    while low<=high:
      minute = low+(high-low)//2 
      if self.possible(battries,minute,n): 
        ans = minute 
        low=minute+1 
      else:
        high=minute-1 
    return ans 
      