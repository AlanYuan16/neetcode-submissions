class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        longest = 0

        for i, num in enumerate(nums):
            if (num - 1) in n:
                continue
            leng = 0                
            while (num + leng) in n:
                leng += 1
                longest = max(leng, longest)
        return longest