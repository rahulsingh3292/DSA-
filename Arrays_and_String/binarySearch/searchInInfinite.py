class Solution:
    def binarySearch(self, arr: list[int], low: int, high: int, target: int) -> int:

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def search(self, arr: list[int], target: int) -> int:
        low = 0
        high = 1
        while arr[high] < target:

            low = high
            high *= 2

        return self.binarySearch(arr, low, high, target)


search = Solution().search
arr = [1, 3, 5, 8, 10, 12, 15, 17]
print(search(arr, 17))
