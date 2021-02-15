def taskAssignment(k, tasks):
    tasks = sorted(enumerate(tasks), key=lambda task:task[1])
    return [[tasks[j][0], tasks[len(tasks)-1-j][0]] for j in range(k)]