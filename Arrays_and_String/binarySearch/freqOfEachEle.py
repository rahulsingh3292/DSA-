class Solution:
    def search(self, arr, low, high, target, is_search_for_last=False):
        ans = low
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                ans = mid
                if is_search_for_last:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if is_search_for_last:
                    high = mid - 1
                else:
                    low = mid + 1
        return ans

    def solve(self, arr):
        index = 0
        count = {}
        while index < len(arr):

            first = self.count(arr, index, len(arr) - 1, arr[index])
            last = self.count(arr, index, len(arr) - 1, arr[index], True)
            count[arr[index]] = (last - first) + 1
            index = last + 1
        return count

    def Findfrequency(self, arr):
        return self.solve(arr)


frequency = Solution().Findfrequency
arr = [1, 2, 3, 4, 7, 7, 7, 8, 9, 9, 9]
print(fr(arr))
