class Solution:
    def possible(self, arr, k):
        if k == 0:
            return 0
        count = 0
        for n in arr:
            count += (n - 1) // k
        return count <= k

    def miniMumSize(self, arr, maxOp):
        low = 0
        high = sum(arr)
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if self.possible(arr, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
