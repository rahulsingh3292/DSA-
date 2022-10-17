
class Solution:
  def helper(self,num,place):
    x = num*place
    if place == 10: 
      if x>=60 and x < 90:
        return "L"+"X"*(num-5)
      elif x == 40:return "XL" 
      elif x == 50: return "L" 
      elif x == 90: return "XC"
      else:
        return "X"*(num)
    elif place == 100:
      if x==500: return "D"
      if x == 100: return "C"
      if x >= 400 and x<500: return "CD"
      elif x>=600 and x<900: return "D"+"C"*(num-5)
      elif x < 400: return "C"*num 
      else: return "CM"
    else: return "M"*num 
    
    
  def integerToRoman(self,n):
    data = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",100:"C",200:"CC",300:"CCC",400:"CD",500:"DC",600:"DCC",700:"DCC",800:"DCCC",900:"CM",1000:"M",2000:"MM",3000:"MMM"}
    if data.get(n): return data.get(n)
    place = 1 
    res = list()
    while n:
      digit = (n%10)
      if data.get(digit) and place==1:
        res.append(data.get(digit)) 
      else:
        res.append(self.helper(digit,place))
      n=n//10 
      place*=10
    return "".join(reversed(res))

res = 599
res = Solution().integerToRoman(i)
 