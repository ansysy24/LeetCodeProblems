
def group_by_and_alphabet(arr):
    dct = {}
    for item in arr:
        dct[item] = dct.get(item, 0) + 1

    return list(sorted(dct.items(), key=lambda x: (-x[1], x[0])))


print(group_by_and_alphabet(['a', 'a', 'a', 'c', 'c', 'c', 'd', 'd', 'b', 'b', 'b']))
