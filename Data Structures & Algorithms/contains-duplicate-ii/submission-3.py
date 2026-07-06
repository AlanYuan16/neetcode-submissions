class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        l = 0

        for i in range(len(nums)):
            if nums[i] in m:
                res = abs(i - m[nums[i]]) 
                if res <= k:
                    return True
            m[nums[i]] = i

        return False