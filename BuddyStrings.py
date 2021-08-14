class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return max(collections.Counter(s).values()) > 1

        swap = ''
        swap_completed = False
        for i in range(len(s)):
            if s[i] != goal[i]:
                if not swap:
                    swap = s[i] + goal[i]
                elif swap_completed:
                    return False
                elif swap != goal[i] + s[i]:
                    return False
                else:
                    swap_completed = True
        return swap_completed