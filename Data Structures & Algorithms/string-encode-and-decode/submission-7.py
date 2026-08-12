class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            leng = int(s[i:j]) #Non including index J
            res.append(s[j + 1 : j + 1 + leng])
            i = j + leng + 1
        return res