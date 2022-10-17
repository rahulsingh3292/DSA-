from tree_data import root 

class Solution:
  def find(self,root,target,curr,
  ans_list,curr_list):
    if root is None: 
      return
    
    curr +=root.data 
    curr_list.append(root.data) 
    
    if root.left is None and root.right is None and curr == target:
      ans_list.append([n for n in curr_list])
    
    self.find(root.left,target,curr,ans_list,curr_list)
    self.find(root.right,target,curr,ans_list,curr_list)
    curr_list.pop()
    
  def pathSum (self,root,target):
    ans_list,curr_list= list(),list()
    curr = 0 
    self.find(root,target,curr,ans_list,curr_list)
    return ans_list 
 
target = 18 
res = Solution().pathSum(root,target)
print(res)