class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        ships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (i, j) not in visited:

                    ships += 1
                    m = i
                    n = j
                    while m < len(board) - 1 and board[m + 1][j] == 'X':
                        visited.add((m + 1, j))
                        m += 1
                    while n < len(board[0]) - 1 and board[i][n + 1] == 'X':
                        visited.add((i, n + 1))
                        n += 1

                visited.add((i, j))

        return ships