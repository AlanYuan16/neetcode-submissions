class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         # Optimal by computing prefix and suffix products
        length = len(nums)
        output = [1] * length

        # Step 1: prefix products
        prefix = 1
        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]
        
        # Step 2: suffix products
        suffix = 1
        for i in range(length-1, -1, -1):# Starting from the last element in the array
            output[i] *= suffix
            suffix *= nums[i]


        return output
        