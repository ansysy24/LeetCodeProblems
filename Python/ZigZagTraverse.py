def zigzagTraverse(array):
    if len(array) == 1:
        return array[0]
    result = [array[0][0], array[1][0]]
    x = 0
    y = 1
    up = True

    while y < len(array) - 1 or x < len(array[0]) - 1:
        if x == len(array[0]) - 1 and up:
            y += 1
            up = False
        elif y == len(array) - 1 and not up:
            x += 1
            up = True
        elif x == 0 and not up:
            y += 1
            up = True
        elif y == 0 and up:
            x += 1
            up = False
        elif up:
            x += 1
            y -= 1
        else:
            x -= 1
            y += 1

        result.append(array[y][x])

    return result

print(zigzagTraverse([
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
  ]))
