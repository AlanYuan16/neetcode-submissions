class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        c_map = {}
        l = 0
        for r in range(len(s)):
            c_map[s[r]]= c_map.get(s[r], 0) + 1

            while (r - l + 1) - max(c_map.values()) > k:
                c_map[s[l]] -= 1
                l += 1
            res = max(res,r - l + 1 )
        return res
