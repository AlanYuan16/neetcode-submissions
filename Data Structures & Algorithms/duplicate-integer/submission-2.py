class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        
        for val in nums:
            s.add(val)
        
        return len(s) != len(nums)