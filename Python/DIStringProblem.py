class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = []
        left = 0
        right = len(s)
        for char in s:
            if char == 'D':
                result.append(right)
                right -= 1
            else:
                result.append(left)
                left += 1

        return result + [right] if s[-1] == 'I' else result + [left]