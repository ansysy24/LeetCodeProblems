def riverSizes(matrix):
    rivers = []
    visited = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] and (i, j) not in visited:
                current_river = 1
                visited.add((i, j))
                next_steps = [(i, j)]
                while next_steps:
                    step = next_steps.pop(0)
                    if step[0]-1 >= 0 and matrix[step[0]-1][step[1]] and (step[0]-1, step[1]) not in visited:
                        next_steps.append((step[0]-1, step[1]))
                        visited.add((step[0]-1, step[1]))
                        current_river += 1
                    if step[0]+1 < len(matrix) and matrix[step[0]+1][step[1]] and (step[0]+1, step[1]) not in visited:
                        next_steps.append((step[0]+1, step[1]))
                        visited.add((step[0]+1, step[1]))
                        current_river += 1
                    if step[1]-1 >= 0 and matrix[step[0]][step[1]-1] and  (step[0], step[1]-1) not in visited:
                        next_steps.append((step[0], step[1]-1))
                        visited.add((step[0], step[1]-1))
                        current_river += 1
                    if step[1]+1 < len(matrix[0]) and matrix[step[0]][step[1]+1] and  (step[0], step[1]+1) not in visited:
                        next_steps.append((step[0], step[1]+1))
                        visited.add((step[0], step[1]+1))
                        current_river += 1
                rivers.append(current_river)
    return rivers