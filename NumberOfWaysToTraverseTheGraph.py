def numberOfWaysToTraverseGraph(width, height, dct={}):
    if width == 1 or height == 1:
        return 1
    dct[(width, height)] = dct.get((width, height), numberOfWaysToTraverseGraph(width-1, height, dct) + numberOfWaysToTraverseGraph(width, height-1, dct))
    return dct[(width, height)]


def numberOfWaysToTraverseGraph2(width, height, dct={}):
    ways = [1 for _ in range(width)]
    for i in range(1, height):
        for j in range(1, len(ways)):
            ways[j] = ways[j] + ways[j - 1]

    return ways[-1]

print(numberOfWaysToTraverseGraph2(4,3), numberOfWaysToTraverseGraph(4,3))

