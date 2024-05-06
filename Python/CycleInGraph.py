def cycleInGraph(edges):
    for i, edge in enumerate(edges):
        level = [i]
        visited = set([i])
        while level:
            nxt = level.pop(0)
            for k in edges[nxt]:
                if k not in visited:
                    level.append(k)
                visited.add(k)
                if k == i:
                    return True
    return False

print(cycleInGraph([[1], [2, 3, 4, 5, 6, 7], [], [2, 7], [5], [], [4], []]))
