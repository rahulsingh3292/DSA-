class Solution:
  def solve(self,fruits):
    n = len(fruits)
    basket={} 
    i=j=0 
    size = 0 
    while j<n:
      type_fruit = fruits[j] 
      if type_fruit not in basket:
        basket[type_fruit] = 1 
      else:
        basket[type_fruit]+=1 
      
      if len(basket)>2:
        while len(basket)>2:
          basket[fruits[i]]-=1 
          if basket[fruits[i]] == 0:
            basket.pop(fruits[i])
          i=i+1
      else:
        size = max(size,(j-i)+1)
      j=j+1
    return size
 

fruits = [0,1,2,2]
Solution().solve(fruits)