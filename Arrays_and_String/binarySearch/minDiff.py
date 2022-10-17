import math


class Solution:
    def minDifference(self, arr: list[int], k: int) -> int:

        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == k:
                return k

            elif k > arr[mid] and k < arr[mid + 1]:
                a, b = abs(arr[mid] - k), abs(arr[mid + 1] - k)
                return arr[mid] if a < b else arr[mid + 1]

            elif k < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return ans


minDiff = Solution().minDifference
arr = [1, 4, 8, 10, 15]
print(minDiff(arr, 3))
