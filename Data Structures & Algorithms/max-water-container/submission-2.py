class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force
        max_area = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                curr = min(heights[l], heights[r]) * (r - l)
                max_area = max(curr, max_area)
        return max_area




