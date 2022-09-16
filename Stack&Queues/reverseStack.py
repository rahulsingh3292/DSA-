def insert(stack,val):
  if not stack:
    stack.append(val)
    return stack
    
  e = stack.pop()
  x = insert(stack,val)
  x.append(e)
  return x 
   
def reverseStack(stack):
  if not stack:
    return stack
  element = stack.pop() 
  reverseStack(stack)
  insert(stack,element)

x = [1,2,3]
reverseStack(x)
print(x)
  