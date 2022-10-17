class Solution:
    def possible(self, arr, capacity, days):
        d = 1
        _sum = 0
        for n in arr:
            if _sum + n <= capacity:
                _sum += n
            else:
                d += 1
                _sum = n
        return d <= days

    def shipWithinDays(self, arr, days):
        low = max(arr)
        high = sum(arr)
        ans = 0
        while low <= high:
            capacity = low + (high - low) // 2

            is_possible = self.possible(arr, capacity, days)
            if is_possible:
                ans = capacity
                high = capacity - 1
            else:
                low = capacity + 1
        return ans
