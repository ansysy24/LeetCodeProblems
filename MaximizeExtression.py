def maximizeExpression(array):
    if len(array) < 4:
        return 0

    a = array[0]
    b = array[1]
    ab = [0]
    i = 1
    while i < len(array) - 2:
        b = min(b, array[i])
        ab.append(a - b)
        a = max(a, array[i])
        i += 1
    ab += [0, 0]

    mxs = []
    mx = array[0]
    for num in array:
        mx = max(mx, num)
        mxs.append(mx)

    mx1 = ab[1]
    for i in range(2, len(mxs) - 1):
        mx1 = max(mx1, ab[i - 1] + mxs[i])
        ab[i] = mx1

    mns = []
    mn = array[-1]
    for num in array:
        mn = min(mn, num)
        mns.append(mn)

    mx2 = ab[2]
    for i in range(3, len(mns)):
        mx2 = max(mx2, ab[i - 1] + mns[i])


    return mx2