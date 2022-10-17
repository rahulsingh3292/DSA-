"""
1-> sort the stalls (req for checking distance) .. 
2-> choose high = max(stalls) 
3-> check for distance(mid).. 
4-> set lastPos=stalls[0] and cows=1 
5-> loop-> n 
6-> check if stalls[i] - lastPos >= given_distance then cow+1 and check if cow==required_cow then return True.. 
  else: set lastPos=current stalls[i]
 
"""


class Solution:
    def possible(self, arr, dist, k):
        cow = 1
        lastPos = arr[0]
        for n in arr:
            if n - lastPos >= dist:
                cow += 1
                if cow == k:
                    return True
                lastPos = n

        return False

    def bSearch(self, arr, low, high, k, ans=-1):
        if low <= high:
            dist = low + (high - low) // 2

            if self.isPossible(arr, dist, k):
                ans = dist
                return self.bSearch(arr, dist + 1, high, k, ans)
            return self.bSearch(arr, low, dist - 1, ans)

        return ans

    def agressiveCows(self, arr, k):
        arr.sort()
        return self.bSearch(arr, k, 0, max(arr))
