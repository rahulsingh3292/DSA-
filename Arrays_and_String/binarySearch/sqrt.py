class Solution:
    def sqrt(self, x: int) -> int:

        low = 1
        high = x
        while low <= high:
            mid = low + (high - low) // 2

            sqrtX = mid * mid

            if sqrtX == x or (sqrtX < x and ((mid + 1) * (mid + 1)) > x):
                return mid

            elif sqrtX < x:
                low = mid + 1
            else:
                high = mid - 1
