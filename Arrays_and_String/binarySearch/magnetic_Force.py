class Solution:
    def possible(self, arr, dist, M):
        ball = 1
        lastPos = arr[0]
        for pos in arr:
            if pos - lastPos >= dist:
                ball += 1
                if ball == M:
                    return True
                lastPos = pos
        return False

    def bSearch(self, arr, low, high, target, ans=0):
        if low <= high:
            dist = low + (high - low) // 2
            if self.possible(arr, dist, target):
                ans = dist
                return self.bSearch(arr, dist + 1, high, target, ans)
            return self.bSearch(arr, low, dist - 1, targans)
        return ans

    def maxDistance(self, arr, M):
        arr.sort()
        return self.bSearch(arr, 0, arr[-1], M)
