class Solution:
    def judgeCircle(self, moves: str) -> bool:
        al = 0
        lo = 0
        for move in moves:
            if move == 'R':
                lo += 1
            elif move == 'L':
                lo -= 1
            elif move == 'U':
                al -= 1
            else:
                al += 1
        return al == 0 and lo == 0