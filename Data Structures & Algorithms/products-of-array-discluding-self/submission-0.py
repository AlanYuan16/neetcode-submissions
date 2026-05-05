class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force
        length = len(nums)
        output = [0] * length

        for i in range(length):
            prod = 1
            for j in range(length):
                if i == j:
                    continue
                prod *= nums[j]
            output[i] = prod
        return output