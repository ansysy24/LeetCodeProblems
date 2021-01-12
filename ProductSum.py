def productSum(array, m=1):
    sum = 0
    for element in array:
        if not type(element) == int:
            sum += m * productSum(element, m + 1)
        else:
            sum += m * element
    return sum

print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
