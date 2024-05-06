def removeIslands(matrix):
    visited = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] and (i, j) not in visited:
                is_island = True
                steps = [(i, j), ]
                current_visited = [(i, j), ]
                while steps:
                    step = steps.pop(0)
                    visited.append((step[0], step[1]))
                    current_visited.append((step[0], step[1]))
                    if step[0] in [0, len(matrix) - 1] or step[1] in [0, len(matrix[0]) - 1]:
                        is_island = False

                    if step[0] - 1 >= 0 and matrix[step[0] - 1][step[1]] and (step[0] - 1, step[1]) not in visited:
                        steps.append((step[0] - 1, step[1]))
                    if step[0] + 1 < len(matrix) and matrix[step[0] + 1][step[1]] and (step[0] + 1, step[1]) not in visited:
                        steps.append((step[0] + 1, step[1]))
                    if step[1] - 1 >= 0 and matrix[step[0]][step[1] - 1] and (step[0], step[1] - 1) not in visited:
                        steps.append((step[0], step[1] - 1))
                    if step[1] + 1 < len(matrix[0]) and matrix[step[0]][step[1] + 1] and (
                    step[0], step[1] + 1) not in visited:
                        steps.append((step[0], step[1] + 1))
                if is_island:
                    for s in current_visited:
                        matrix[s[0]][s[1]] = 0
    return matrix

print(removeIslands([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]))