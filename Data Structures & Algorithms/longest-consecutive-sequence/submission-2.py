class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in s:
                leng = 0
                while (n + leng) in s:
                    leng += 1
                    longest = max(leng,longest)
        return longest