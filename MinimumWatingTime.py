def minimumWaitingTime(queries):
    if len(queries) < 2:
        return 0
    queries.sort()
    result = [queries[0]]
    nxt = queries[0]
    for num in queries[1:-1]:
        nxt += num
        result.append(nxt)
    return sum(result)

print(minimumWaitingTime([6,2,3,2,1]))