class Solution:
    def is_valid(self, arr: list[int], n: int, k: int) -> bool:
        student: int = 1
        _sum: int = 0
        for pages in arr:
            _sum += pages
            if _sum > n:
                student += 1
                _sum = pages

            if student > k:
                return False

        return True

    def findPages(self, arr: list[int], k: int) -> int:
        n: int = len(arr)
        if n < k:
            return -1
        if n == k:
            return max(arr)
        low: int = max(arr)
        high: int = sum(arr)
        ans: int = -1
        while low <= high:
            mid: int = low + (high - low) // 2

            if self.is_valid(arr, mid, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


allocate = Solution().findPages
print(allocate([10, 20, 30, 40, 50], 3))
