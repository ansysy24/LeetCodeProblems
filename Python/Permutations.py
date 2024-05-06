def getPermutations(array):
    if not array:
        return []
    permutations = []
    helper(array, permutations)
    return permutations

def helper(array, permutations, current = []):
    if not array:
        permutations.append(current)
		
    for i, number in enumerate(array):
        new_perm = current.copy() + [number]
        helper(array[:i] + array[i+1:], permutations, new_perm)

print(getPermutations([1,2,3]))
