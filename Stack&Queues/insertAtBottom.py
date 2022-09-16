
def insert(stack,data):
  if not stack:
    stack.append(data)
    return stack
    
  element = stack.pop()
  res = insert(stack,data)
  res.append(element)
  return res 

print(insert([1,2,3],4))