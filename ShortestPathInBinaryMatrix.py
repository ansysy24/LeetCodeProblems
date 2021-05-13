class Solution:
    def change_state(self, i, j, counter):
        if (i, j) not in self.visited:
            self.visited.add((i, j))
            self.steps.append((i, j, counter))

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        i = 0
        j = 0

        self.steps = [(i, j, 0)]
        self.visited = set([(i, j)])

        while self.steps[0][0] < len(grid) - 1 and self.steps[0][1] < len(grid[0]) - 1:
            step = self.steps.pop(0)
            k = step[0]
            l = step[1]
            counter = step[2]
            if k < len(grid) - 1 and grid[k + 1][l - 1] == 0:
                self.change_state(k + 1, l, counter + 1)

            if l < len(grid[0]) - 1 and grid[k][l + 1] == 0:
                self.change_state(k, l + 1, counter + 1)

            if k < len(grid) - 1 and l < len(grid[0]) - 1 and grid[k + 1][l + 1] == 0:
                self.change_state(k + 1, l + 1, counter + 1)

            if k > 0 and grid[k - 1][step[l]] == 0:
                self.change_state(k - 1, l, counter + 1)

            if l > 0 and grid[k][l - 1] == 0:
                self.change_state(k, l - 1, counter + 1)

            if l > 0 and k > 0 and grid[k - 1][l - 1] == 0:
                self.change_state(k - 1, l - 1, counter + 1)

            if k > 0 and l < len(grid[0]) - 1 and grid[k - 1][l + 1] == 0:
                self.change_state(k - 1, l + 1, counter + 1)

            if k < len(grid) - 1 and l > 0 and grid[k + 1][l - 1] == 0:
                self.change_state(k + 1, l - 1, counter + 1)

        return self.steps[0][2]