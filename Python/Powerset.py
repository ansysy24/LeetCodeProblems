def powerset(array):
	final_powerset = [[]]
	helper(array, final_powerset)
	return final_powerset

def helper(array, final_powerset, current_list = []):
	if not array:
		current_list = []
	
	for i, number in enumerate(array):
		new_list = current_list + [number]
		final_powerset.append(new_list)
		helper(array[i+1:], final_powerset, new_list)

print(powerset([1,2,3,4]))
