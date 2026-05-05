class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_arr = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and sorted_arr[i] == sorted_arr[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = sorted_arr[i] + sorted_arr[l] + sorted_arr[r] 
                if 0 > total:
                    l += 1
                elif 0 < total:
                    r -= 1
                else:
                    result.append([sorted_arr[i], sorted_arr[l], sorted_arr[r]])
                    r -= 1
                    l += 1

                    while l < r and sorted_arr[l] == sorted_arr[l - 1]:
                        l += 1
                    while l < r and sorted_arr[r] == sorted_arr[r + 1]:
                        r -= 1
        return result