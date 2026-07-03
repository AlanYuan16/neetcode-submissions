class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        longest = 0
        for num in nums:
            leng = 0
            if (num - 1) not in n:
                
                while (num + leng) in n:
                    leng += 1
                longest = max(leng, longest)
        return longest