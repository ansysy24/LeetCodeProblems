class Solution:
    def secondHighest(self, s: str) -> int:
        l1 = float('-inf')
        l2 = float('-inf')
        for char in s:
            if char.isnumeric():
                num = int(char)
                if l1 < num:
                    l2 = l1
                    l1 = num
                elif l2 < num and l1 != num:
                    l2 = num
        return l2 if l2 != float('-inf') else -1