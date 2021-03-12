class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = sorted(zip(s, indices), key=lambda x:x[1])
        return ''.join([e[0] for e in lst])