class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        slow, fast = nums[0], nums[0]

         # Phase 1: find intersection point in the cycle
        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

         # Phase 2: find entrance to the cycle (the duplicate)
        slow2 = nums[0]
        while slow2 != slow:

            slow2 = nums[slow2]
            slow = nums[slow]

        return slow