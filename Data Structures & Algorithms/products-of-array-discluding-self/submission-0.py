class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))
        postF = 1
        preF = 1
        for i in range(len(nums)):
            res[i] = preF
            preF *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postF
            postF *= nums[i]
        return res