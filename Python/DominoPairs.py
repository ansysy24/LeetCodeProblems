class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dct = {}
        for dom in dominoes:
            key = tuple(sorted(dom))
            dct[key] = dct.get(key, 0) + 1
        pairs = 0
        for k in dct:
            if dct[k] > 1:
                val = dct[k]
                pairs += (val*val - val)/2
        return int(pairs)