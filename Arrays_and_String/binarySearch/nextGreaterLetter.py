class Solution:
    def nextGreaterLetter(self, letters: list[str], target: str) -> str:

        low: int = 0
        high: int = len(letters) - 1
        ans: str = letters[0]
        while low <= high:
            mid: int = low + (high - low) // 2

            if arr[mid] > target:
                ans = arr[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans
