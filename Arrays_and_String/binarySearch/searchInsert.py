class Solution:
    def searchInsert(self, arr: list[int], target: int) -> int:

        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == target:
                return mid

            elif target > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low
