
class Solution:

    
  def chalkReplacer(self,chalk: list[int], n: int)-> int:
    
    remian_chalks = n 
    _sum = sum(chalk)
    if remian_chalks > _sum:
      remian_chalks = n%_sum 
    
    for i in range(len(chalk)):
      if chalk[i] <= remian_chalks:
        remian_chalks-= chalk[i] 
      else: return i 
    # for the last test case.. 
    return 0 
    

    
    
