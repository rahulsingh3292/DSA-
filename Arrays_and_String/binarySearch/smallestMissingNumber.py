class Solution:
    def smallestMissing(self, arr: list[int]) -> int:
        arr.sort()
        low = 0
        high = len(arr)
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] == mid:
                low = mid + 1
            else:
                high = mid
        return high
