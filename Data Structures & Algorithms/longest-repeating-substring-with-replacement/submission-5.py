class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        seen = {}
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while (r - l + 1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
        return longest