

from collections import deque 
def modifyQueue(Q,k):
    stack = deque([Q[i] for i in range(k)]) 
    for i in range(k):
      Q[i] = stack.pop() 
    return Q 