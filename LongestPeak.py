def longestPeak(array):
    if len(array) < 3:
        return 0
    j = 0
    while array[0] >= array[1]:
        array.pop(0)

    max_ln = 0
    ln = 1
    up = True
    peak = False

    for i, num in enumerate(array[1:]):

        if num == array[i]:
            if peak:
                max_ln = max(ln, max_ln)
                peak = False
            ln = 1

        elif up == True:
            if num < array[i]:
                up = False
                peak = True
                max_ln = max(ln, max_ln)
            ln += 1

        else:
            if num > array[i]:
                up = True
                if peak:
                    max_ln = max(ln, max_ln)
                peak = False
                ln = 1
                continue
            ln += 1

        print(ln)

    return max(ln, max_ln)