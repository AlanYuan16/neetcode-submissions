class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                leng = 1
                current = num

                while current + 1 in s:
                    leng += 1
                    current += 1
                longest = max(longest, leng)

        return longest
        