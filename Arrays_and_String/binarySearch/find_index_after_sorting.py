class Solution:
    def targetIndices(self, arr: List[int], target: int) -> List[int]:
        arr.sort() 
        low = 0 
        high=len(arr)-1
        while low<=high:
          mid = low+(high-low)//2 
          
          if arr[mid]==target:
            result = [] 
            result.append(mid)
            i=mid
            j=mid 
            while i>0 and arr[i-1] == target:
              result.append(i-1) 
              i-=1
            while j+1<len(arr) and arr[j+1]==target:
              result.append(j+1) 
              j+=1 
            return sorted(result) 
            
            
          elif arr[mid]>target:
            high=mid-1 
          else:
            low=mid+1
        return () 