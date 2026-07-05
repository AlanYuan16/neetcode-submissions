class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        res = -1 
        for n in c:
            if n == c.get(n):
                res = max(n, res)
        return res