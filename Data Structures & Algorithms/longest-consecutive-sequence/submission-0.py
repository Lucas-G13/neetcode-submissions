class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestStreak = 0
        currentStreak = 0
        for num in nums:
            if num - 1 not in nums:
                currentStreak = 1
                nextNum = num + 1
                while nextNum in nums:
                    currentStreak += 1
                    nextNum += 1
                longestStreak = max(currentStreak, longestStreak)
        return longestStreak