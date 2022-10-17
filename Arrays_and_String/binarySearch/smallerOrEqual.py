class Solution:
    def smallerOrEqual(self, arr: list[int], target: int) -> int:
        low: int = 0
        high: int = len(arr) - 1
        total = 0
        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] <= target:
                total = mid + 1
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def solve(self, arr, target):
        return self.smallerOrEqual(arr, target)
