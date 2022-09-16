class Solution:
  def maxProfit (self,prices):
    n = len(prices)
    minimum_price = prices[0] 
    max_profit = 0 
    current_max = 0 
    
    i = 1 
    while i < n:
      j = i 
      while j<n and prices[j] -minimum_price > current_max:
        current_max = prices[j] - minimum_price 
        j+=1 
        
      max_profit +=current_max
      minimum_price= prices[j] if j<n else 0
      current_max=0
      i=j+1
    return max_profit 
      
      
    
      
    
    

prices =[1,2,3,9,10,12,5,6,10] 
print(Solution().maxProfit(prices))