def taskAssignment(k, tasks):
    tasks = sorted(enumerate(tasks), key=lambda task: task[1])
    return [[tasks[j][0], tasks[len(tasks)-1-j][0]] for j in range(k)]

print(taskAssignment(7, [2, 1, 3, 4, 5, 13, 12, 9, 11, 10, 6, 7, 14, 8]))