class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sort = sorted(nums)

        for i in range(1, len(sort)):
            if sort[i] == sort[i - 1]:
                return True
        
        return False