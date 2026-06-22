class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        out = [0] * leng

        for i in range(leng):
            prod = 1
            for j in range(leng):
                if i == j:
                    continue
                prod *= nums[j]
            out[i] = prod
        return out