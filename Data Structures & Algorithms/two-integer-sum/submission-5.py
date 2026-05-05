'''
def twoSum(nums, target):
    seen = {} # Dictionary: num -> index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            # If the complement is found, return its index and the current index
            return [seen[diff], i] 
        # Otherwise, store the current number and its index in the map
        seen[num] = i
    return [] # As the problem guarantees a solution, this line is often not reached

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i
        return []