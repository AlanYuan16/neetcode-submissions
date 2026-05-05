class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for val in nums:
            s.add(val)
        
        if len(s) != len(nums):
            return True
        
        return False