class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       group_map = defaultdict(list)
       for s in strs:
        key = tuple(sorted(s))
        group_map[key].append(s)
       return list(group_map.values())


        