class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            lookup[key].append(s)
        return list(lookup.values())