class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_container = 0
        while l < r:
            max_container = max((r - l) * min(heights[l], heights[r]), max_container)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_container
            
