class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Count_S = Counter(s)
        Count_T = Counter(t)

        return Count_T == Count_S