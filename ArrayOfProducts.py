def arrayOfProducts(array):
    left = [1 for _ in array]
    right = [1 for _ in array]
    val = 1
    for i in range(len(array)):
        val *= array[i]
        left[i] = val

    val = 1
    for i in range(len(array) - 1, -1, -1):
        val *= array[i]
        right[i] = val

    products = []
    for i in range(len(array)):
        left_prod = 1 if i - 1 < 0 else left[i - 1]
        right_prod = 1 if i + 1 > len(array) - 1 else right[i + 1]
        products.append(left_prod * right_prod)
    return products

print(arrayOfProducts([9, 3, 2, 1, 9, 5, 3, 2]))