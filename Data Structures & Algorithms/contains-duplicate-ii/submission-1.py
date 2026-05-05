class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        l = 0

        for r in range(len(nums)):
            if nums[r] in m:
                distance = abs(r - m[nums[r]])
                if distance <= k:
                    return True
            
            m[nums[r]] = r
        return False

