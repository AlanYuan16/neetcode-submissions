class Solution:
    def isPalindrome(self, s: str) -> bool:
        out = ""

        for c in s:
            if c.isalnum():
                out += c.lower()
        return out == out[::-1]