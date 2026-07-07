class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        for nums, count in c.items():
            if count > 1:
                return nums