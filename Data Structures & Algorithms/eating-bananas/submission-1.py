class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_p = max(piles)
        min_p = 1
        p = max_p

        while min_p <= max_p:
            mid_p = (max_p + min_p) // 2
            counter = 0
            for m in piles:
                counter += math.ceil(m / mid_p)
            if counter <= h:
                p = mid_p
                max_p = mid_p - 1
            else:
                min_p = mid_p + 1
        return p