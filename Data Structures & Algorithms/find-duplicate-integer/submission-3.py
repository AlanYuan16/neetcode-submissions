class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Start both pointers at the same place (treat nums[0] as entry point)
        slow = fast = nums[0]

        # Take the first hop before the loop so slow != fast initially
        # (otherwise the while loop below would exit immediately)
        slow = nums[slow]           # slow moves 1 step
        fast = nums[nums[fast]]     # fast moves 2 steps

        # Phase 1: keep hopping until slow and fast land on the same index
        # This is guaranteed to happen since a cycle must exist
        # (pigeonhole principle: n+1 numbers, values only in range [1, n])
        while slow != fast:
            slow = nums[slow]           # 1 hop
            fast = nums[nums[fast]]     # 2 hops
        # At this point, slow and fast have met SOMEWHERE inside the cycle
        # (not necessarily at the start of the cycle)

        # Phase 2: find the entrance of the cycle
        # Reset slow back to the start, keep fast where it is
        slow = nums[0]

        # Move both pointers 1 step at a time
        # They are mathematically guaranteed to meet exactly at the
        # entrance of the cycle, which is the duplicate number
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # Both pointers now point to the duplicate value
        return slow