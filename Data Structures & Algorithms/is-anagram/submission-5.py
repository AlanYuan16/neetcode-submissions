class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        S_Count, T_Count = {}, {}

        for c in range(len(s)):
            S_Count[s[c]] = S_Count.get(s[c], 0) + 1
            T_Count[t[c]] = T_Count.get(t[c], 0) + 1
        
        return S_Count == T_Count
