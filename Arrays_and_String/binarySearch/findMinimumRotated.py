class Solution:
    def findMin(self, arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2

            if arr[mid] > arr[mid + 1]:
                return mid + 1
            else:
                if arr[mid] > arr[high]:

                    low = mid + 1
                else:
                    high = mid

        return arr[high]


search = Solution().findMin
ans = search([4, 1, 2, 3])
print(ans)
