def maximizeExpression(array):
    if len(array) < 4:
        return 0
    sm = float('-inf')

    for i, num in enumerate(array[:-3]):
        for j, num2 in enumerate(array[i + 1:-2]):
            for k, num3 in enumerate(array[i + 1 + j + 1:-1]):
                for m, num4 in enumerate(array[i + 1 + j + 1 + k + 1:]):
                    sm = max(sm, num - num2 + num3 - num4)

    return sm