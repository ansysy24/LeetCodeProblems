def fourNumberSum(array, target):
    quadr = []
    pairs = {}

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            correspond = target - array[i] - array[j]
            if correspond in pairs:
                for pair in pairs[correspond]:
                    quadr.append(pair + [array[i]] + [array[j]])

        for k in range(i):
            pairs[array[k] + array[i]] = pairs.get(array[k] + array[i], []) + [[array[k], array[i]]]

    return quadr