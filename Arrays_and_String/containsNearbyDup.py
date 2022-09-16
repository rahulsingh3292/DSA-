class Solution:
  def containsNearbyDuplicate(self,arr,k):
    
    data = {} 
    for idx,value in enumerate(arr):
      """
      idx = index 
      data[value] return previous index 
      ---------------------------------
      checking if the current value present in 
      map. then check if their index  of absolute diff<=k. of it's satisfying the cond then return True .. otherwise their abs diff is > k.. so update this prev index to current index.. for next future calls.. 
      """ 
      if data.get(value) is not None :
        if abs(data[value]-idx)<=k:
          return True 
        # updating previosu index to current index.. 
        data[value]=idx
      else:
        # the value not present in map so add to map
        data[value] = idx 
    return False 