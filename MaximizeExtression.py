def maximizeExpression(array):
    if len(array) < 4:
        return 0

    max_as = []
    max_a = array[0]
    for num in array:
        max_a = max(max_a, num)
        max_as.append(max_a)

    max_abs = [None, ]
    max_ab = float('-inf')
    for i in range(len(max_as) - 1):
        max_ab = max(max_ab, max_as[i] - array[i + 1])
        max_abs.append(max_ab)

    max_abcs = [None, None]
    max_abc = float('-inf')
    for i in range(1, len(array) - 1):
        max_abc = max(max_abc, max_abs[i] + array[i + 1])
        max_abcs.append(max_abc)

    max_abcds = [None, None, None]
    max_abcd = float('-inf')
    for i in range(2, len(array) - 1):
        max_abcd = max(max_abcd, max_abcs[i] - array[i + 1])
        max_abcds.append(max_abcd)
    return max_abcds[-1]