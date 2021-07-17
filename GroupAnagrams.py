class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for st in strs:
            key = tuple(sorted(st))
            groups[key] = groups.get(key, []) + [st]
        return list(groups.values())