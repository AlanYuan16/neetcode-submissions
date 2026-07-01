class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force attempt
        out = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    out[i] *= nums[j]
        return out