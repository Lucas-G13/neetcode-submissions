class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_counts = {}
        for i in nums:
            int_counts[i] = int_counts[i] + 1 if (i in int_counts) else 1
        return sorted(int_counts, key=int_counts.get, reverse = True)[:k]