class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        keys = {}

      
        for word in strs:
            key = "".join(sorted(word))

            if key in keys:
                keys[key].append(word)
            else:
                keys[key] = [word]


        return list(keys.values())

            



        

        