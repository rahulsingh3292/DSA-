class  Solution:
  
  def reverseX(self,x):
    reversedInt = 0 
    while x:
      lastDigit = n%10 
      reversedInt = (reversedInt*10)+lastDigit
      x=x//10 
    return reversedInt 
    
  def reverse(self,x):
    MAX_INT = 2147483647 
    MIN_INT = -2147483648 
    
    is_neg = True if x<0 else False 
    if is_neg: 
      if x<=MIN_INT: return 0 
    if x>=MAX_INT: return 0 
    
    x = abs(x) 
    reversedInt = self.reverseX(x)
    if is_neg:
      return -reversedInt if -reversedInt > MIN_INT else 0 
    return reversedInt if reversedInt< MAX_INT else 0 
    
    
    