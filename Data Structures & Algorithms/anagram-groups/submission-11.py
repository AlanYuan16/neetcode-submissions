class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        look_up = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in look_up:
                look_up[key].append(word)
            else:
                look_up[key] = [word]
        return list(look_up.values())