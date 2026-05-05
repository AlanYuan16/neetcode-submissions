class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tableS, tableT = {}, {}

        for c in range(len(s)):
            # access the char by s[c]
            tableS[s[c]] = tableS.get(s[c],0) + 1
            tableT[t[c]] = tableT.get(t[c],0) + 1

        return tableS == tableT