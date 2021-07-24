class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = ')]}'
        correspond = {')': '(', '}': '{', ']': '['}
        for br in s:
            if br in closing:
                if not stack:
                    return False
                elif stack[-1] == correspond[br]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(br)
        return stack == []
