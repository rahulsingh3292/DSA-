# leeetcode => 2064. miniMized the maximum product distributed to any store..


# approach => well select the most highest product..

# loop in quantities and aur quantities ko given product se // krke (q//product) shop ko count krwa le.. aur agar // krne pr bache hai toh usko +1 kr de..

# agar yeh sab hone ke baad shop jyada ho gya toh hum false return krenge nahi yoh True


class Solution:
    def possible(self, arr, n, k):
        if k == 0:
            return 0
        store = 0
        for q in arr:
            store += q // k
            if q % k != 0:
                store += 1
            if store > n:
                return False
        return True

    def minimizedMaximum(self, n, arr):
        low = 0
        high = max(arr)
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            is_possible = self.possible(arr, n, mid)
            if is_possible:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
