class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_m = {}
        s2_m = {}
        window_size = len(s1)
        l,r  = 0, 0
        for s in s1:
            s1_m[s] = s1_m.get(s, 0) + 1

        #build the window
        while r < window_size:
            s2_m[s2[r]] = s2_m.get(s2[r], 0) + 1
            r += 1

        if s1_m == s2_m:
            return True

        while r < len(s2):
            s2_m[s2[r]] = s2_m.get(s2[r], 0) + 1 
            s2_m[s2[l]] -= 1

            if s2_m[s2[l]] == 0:
                del s2_m[s2[l]]
            
            l += 1
            r += 1

            if s1_m == s2_m:
                return True
        return False

            
                        

