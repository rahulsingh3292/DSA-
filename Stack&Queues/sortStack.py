
def insert(stack,val):
  if not stack:
    stack.append(val)
    return stack
    
  element = stack.pop()
  insert(stack,val)
  if stack[-1] > element:
    greater = stack.pop()
    stack.append(element)
    stack.append(greater)
    return 
  stack.append(element)
  
  """
  if element < stack[-1]:
    greater = stack.pop()
    res.append(element)
    res.append(greater)
    return res 
  else:
    res.append(element)
    return res 
  """
def sortStack(stack):
  if not stack:
    return
    
  val = stack.pop()
  sortStack(stack)
  insert(stack,val)


stack = [2,3,-2]
sortStack(stack)
print(stack)