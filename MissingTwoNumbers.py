def find_two_missing_numbers(lst):
    seen_n = False
    seen_n_1 = False
    for num in lst:
        num = abs(num)
        if num-1<len(lst):
            lst[num-1] *= -1
        elif num-1 == len(lst):
            seen_n = True
        else:
            seen_n_1 = True
    result = []
    for i, num in enumerate(lst):
        if num > 0:
            result.append(i+1)
    if not seen_n:
        result.append(len(lst))
    if not seen_n_1:
        result.append(len(lst)+1)

    return result

print(find_two_missing_numbers([1,7,6,2,4]))
