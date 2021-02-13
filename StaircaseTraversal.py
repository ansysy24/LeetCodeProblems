def staircaseTraversal(height, maxSteps):
    return helper(height, maxSteps, {0: 1, 1: 1})


def helper(height, maxSteps, memo):
    if height in memo:
        return memo[height]
    ways = 0
    for i in range(1, min(maxSteps+1, height+1)):
        ways += helper(height-i, maxSteps, memo)
    memo[height] = ways
    return ways


def staircaseTraversal2(height, maxSteps):
    if height < 2:
        return 1
    ways = [0 for i in range(height+1)]
    ways[0] = 1
    ways[1] = 1
    for i in range(2, height+1):
        sm = 0
        end = 0 if i-maxSteps < 0 else i-maxSteps
        for j in range(i-1, end-1, -1):
            sm += ways[j]
        ways[i] = sm
    return ways[-1]