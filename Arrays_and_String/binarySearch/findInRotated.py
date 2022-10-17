class Solution:
    def search(self, arr: list[int], target: int) -> int:

        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] >= arr[low]:
                if target <= arr[mid] and target >= arr[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target >= arr[mid] and target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

    def search(self, arr, target, low, high):
        if low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == target:
                return mid
            if arr[mid] > arr[low]:
                if target >= arr[low] and target <= arr[mid]:
                    return self.search(arr, target, low, mid - 1)
                else:
                    return self.search(arr, target, mid + 1, high)
            else:
                if target >= arr[mid] and target <= arr[high]:
                    return self.search(arr, target, mid + 1, high)
                return self.search(arr, target, low, mid - 1)

        return -1
