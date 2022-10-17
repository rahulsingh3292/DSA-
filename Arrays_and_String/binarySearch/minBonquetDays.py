# Question-> Min number of dayS to make M BouquetS...

# 1-> we'll select the max day from blommDay..

# 2-> and for the given day we'll check in the garden..

# 3-> agar diye hue day par koi flower bloom ho chuka(bloomday[i] <= givenDay) hai toh hum use  flower+=1 kr lenge

#  aur jab count == k ho jayega ..

# toh hum bonquet ka count badha denge and flower ko 0 se initialize kr denge..

# agar bloomday[i] > givenDay then flower ko 0 se initialize kr denge..

# and in last hum  check krenge ki agar bonquet >= reqBonquet hai toh .. iss day ko ans mein add kr lenge... aur isse chote day ko dekhe..


class Solution:
    def possibleWithPresentDay(self, day, bloomdayS, M, K):

        flowers = 0
        current_bonquet = 0
        for bloomday in bloomdayS:
            if bloomday <= day:
                flowers += 1
                if flowers == K:
                    flowers = 0
                    current_bonquet += 1
            else:
                flowers = 0
            if current_bonquet >= M:
                return True
        return current_bonquet >= M

    def minDays(self, bloomdayS, M, K):
        # m-> Required bonquet ..
        # k -> har bucket mein itne flower rhne chhiye..

        # bloomdayS -> n flower jo ki iss dayS pe khil jate hai...

        low = 0
        high = int(1e10)
        ans = -1
        while low <= high:
            day = low + (high - low) // 2
            print()
            if self.possibleWithPresentDay(day, bloomdayS, M, K):
                ans = day
                high = day - 1
            else:
                low = day + 1
        return ans


minDay = Solution().minDays
arr = [7, 7, 7, 7, 12, 7, 7]
print(minDay(arr, 2, 3))
