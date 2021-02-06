def firstDuplicateValue(array):
    for value in array:
        if array[abs(value)-1] < 0:
            return abs(value)
        else:
            array[abs(value)-1] *= -1
    return -1

def firstDuplicateValue2(array):
    st = set()
    for num in array:
        if num in st:
            return num
        st.add(num)
    return -1


arr = [9, 13, 6, 2, 3, 5, 5, 5, 3, 2, 2, 2, 2, 4, 3]

print(firstDuplicateValue2(arr))
print(firstDuplicateValue2(arr) == firstDuplicateValue2(arr))