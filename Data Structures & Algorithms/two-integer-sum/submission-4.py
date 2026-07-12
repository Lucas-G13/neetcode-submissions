class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_match = {}
        for i in range(len(nums)):
            if nums[i] in num_match:
                return [num_match[nums[i]], i]
            else:
                num_match[target - nums[i]] = i
