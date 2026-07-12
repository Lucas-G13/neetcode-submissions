class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_match = {}
        for i in range(len(nums)):
            current_num = nums[i]
            if current_num in num_match:
                return [num_match[current_num], i]
            else:
                num_match[target - current_num] = i
