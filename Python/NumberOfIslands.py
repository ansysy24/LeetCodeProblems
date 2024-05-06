class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    visited.add((i, j))
                    ones = [(i, j)]
                    while ones:
                        a, b = ones.pop(0)
                        if a < len(grid)-1 and (a+1, b) not in visited and grid[a+1][b] == '1':
                            ones.append((a+1, b))
                            visited.add((a+1, b))
                        if a > 0 and (a-1, b) not in visited and grid[a-1][b] == '1':
                            ones.append((a-1, b))
                            visited.add((a-1, b))
                        if b < len(grid[0])-1 and (a, b+1) not in visited and grid[a][b+1] == '1':
                            ones.append((a, b+1))
                            visited.add((a, b+1))
                        if b > 0 and (a, b-1) not in visited and grid[a][b-1] == '1':
                            ones.append((a, b-1))
                            visited.add((a, b-1))
        return islands