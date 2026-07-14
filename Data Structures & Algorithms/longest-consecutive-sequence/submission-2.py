class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestStreak = 0
        currentStreak = 0
        for num in nums:
            if num - 1 not in numSet:
                currentStreak = 1
                nextNum = num + 1
                while nextNum in numSet:
                    currentStreak += 1
                    nextNum += 1
                longestStreak = max(currentStreak, longestStreak)
        return longestStreak