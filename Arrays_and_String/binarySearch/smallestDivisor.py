import math


class Solution:
    def checkDiv(self, arr, div, ts):
        if div == 0:
            return 0
        _sum = 0
        for n in arr:
            _sum += math.ceil(n / div)
        if _sum <= ts:
            return True
        return False

    def smallestDivisor(self, arr, thresold):

        low = 0
        high = max(arr)
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if self.checkDiv(arr, mid, thresold):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


sd = Solution().smallestDivisor
arr = [1, 2, 5, 9]
arr = [44, 22, 33, 11, 1]
print(sd(arr, 5))
