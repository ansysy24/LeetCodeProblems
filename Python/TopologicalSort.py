def topologicalSort(jobs, deps):
    ln = len(jobs)
    answer = []
    j = 0
    while j < ln:
        groups = {}
        for dep in deps:
            groups[dep[0]] = groups.get(dep[1], []) + [dep]

        diff = set(jobs) - set(groups.keys())
        answer = list(diff) + answer
        jobs = set(jobs) - diff

        i = 0
        while i < len(deps):
            if deps[i][1] in diff:
                deps.pop(i)
            else:
                i += 1
        j += 1

        return answer if answer and len(answer) == ln else []

print(topologicalSort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]))