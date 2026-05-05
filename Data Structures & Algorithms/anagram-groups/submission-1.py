class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}
        res = []

        for s in strs:
            key = tuple(sorted(s))
            if key not in group_map:
                group_map[key] = []
            group_map[key].append(s)
        
        return list(group_map.values())
            