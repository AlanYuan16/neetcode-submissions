class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        Count_S, Count_T = {}, {}

        for i in range(len(s)):
            Count_S[s[i]] = Count_S.get(s[i],0) + 1
            Count_T[t[i]] = Count_T.get(t[i], 0) + 1
        return Count_T == Count_S
      