

class Solution:
  def matchPlayersAndTrainers(self,players,trainers):
    players.sort()
    trainers.sort()
    n,m = len(players),len(trainers)
    i=j=count=0
    while i<n and j<m:
      x,y = players[i],trainers[j]
      if x<=y:
        count+=1
        i+=1 
        j+=1 
      elif y < x:
        j=j+1 
      else:
        i=i+1 
      
    return count
     
    
    
x = [4,7,4]
y = [8,2,5,8]
     
Solution().matchPlayersAndTrainers(x,y)
