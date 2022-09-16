from math import sqrt 
from typing import List,Tuple
class Calculator: 
  
  def __init__(self):
    self.max_prime_to_calculate: int = int(1e9)
    self.primes: List[bool] = [True]*self.max_prime_to_calculate
    
  def add(self,x: int,y: int, *args: Tuple[int])-> int:
    result: int = x+y  
    for n in args:
      result +=n 
    return result 

  def power(self,x: int,y: int)-> int:
    if y==0:
      return 1 
    return x*power(x,y-1) 

  def factorial(self,n: int)-> int:
    if n==1:
      return  1
    return n*factorial(n-1)

  def generatePrimes(self)-> None:
    _max: int = self.max_prime_to_calculate
    self.primes[0] = False 
    self.primes[1] = False 
    for i in range(2,int(sqrt(_max)+1)):
      if self.primes[i]:
        for j in range(i*i,
         _max,i):
          self.primes[j] = False 
    
  def isPrime(self,n: int)-> bool:
    return self.primes[n] 
  
  def evenOdd(self,n: int)-> str:
    # & == (%2==0 or 1)
    if n&1:
      return f"{n} is odd number"
    return f"{n} is even number" 
  
math = Calculator() 
math.generatePrimes() 