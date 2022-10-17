class Solution:
    def possible_with_Hi(self, arr, hi, M):
        total = 0
        for n in arr:
            if n > hi:
                total += (n) - hi
        return total >= M

    def cutWood(self, arr, M):
        low = 0
        high = sum(arr)
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2

            if self.possible_with_Hi(arr, mid, M):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def solve(self, arr, M):
        return self.cutWood(arr, M)
