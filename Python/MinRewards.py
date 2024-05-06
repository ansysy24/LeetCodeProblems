def minRewards(scores):

    # edge cases
    if len(scores) == 2:
        return 3
    if len(scores) == 1:
        return 1

    # Creation the array for the indexes of minimums and rewards empty array.
    mins = []
    rewards = [0 for _ in scores]

    # Cheking if start/end of the scores array are minimums
    if scores[0] < scores[1]:
        mins.append(0)
        rewards[0] = 1
        rewards[1] = 2
    if scores[-1] < scores[-2]:
        mins.append(len(scores) - 1)
        rewards[-1] = 1
        rewards[-2] = 2

    # Assigning 1 score to a local minimum and 2's to its sides
    i = 1
    while i < len(scores) - 1:
        if scores[i - 1] > scores[i] < scores[i + 1]:
            mins.append(i)
            rewards[i] = 1
            rewards[i - 1] = 2
            rewards[i + 1] = 2
        i += 1

    # Iterating over each interval with a minimum and assigning rewards
    for mi in mins:
        j = mi - 1
        while j > 0 and scores[j - 1] > scores[j]:
            rewards[j - 1] = rewards[j] + 1
            j -= 1

        j = mi + 1
        while j < len(scores) - 1 and scores[j + 1] > scores[j]:
            rewards[j + 1] = rewards[j] + 1
            j += 1

    return sum(rewards)

print(minRewards([2,3,4,1]))