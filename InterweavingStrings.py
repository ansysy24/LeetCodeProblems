def interweavingStrings(one, two, three):
	if not one + two + three:
		return True
	
	i_check = False
	j_check = False
	if one and three and one[0] == three[0]:
		i_check = interweavingStrings(one[1:], two, three[1:])
	if two and three and two[0] == three[0]:
		j_check =  interweavingStrings(one, two[1:], three[1:])

	return i_check or j_check

print(interweavingStrings('ab', 'ac', 'aabc'))
