def fibonacci(num):
    if num < 3:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(5))


def fibonacci2(num):
    if num < 3:
        return 1

    lst = [1, 1]
    for i in range(3, num):
        lst.append(sum(lst))
        lst.pop(0)
        print(lst)

    return sum(lst)

print(fibonacci2(5))