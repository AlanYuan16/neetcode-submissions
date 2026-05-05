class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Calculate prefix of values before i
        leng = len(nums)
        result = [1] * leng

        prefix = 1

        for i in range(leng):
            result[i] = prefix
            prefix *= nums[i]
        
        #Now Multiply the prefix and suffix

        suffix = 1

        for i in range(leng - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result