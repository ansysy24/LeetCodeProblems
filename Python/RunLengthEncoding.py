def runLengthEncoding(string):
	sequence = ''
	previous_letter = string[0]
	current_num = 1
	for current_letter in string[1:]:
		if current_letter == previous_letter and current_num < 9:
			current_num += 1
		else:
			sequence += f'{current_num}{previous_letter}'
			current_num = 1
			
		previous_letter = current_letter
	
	return sequence + f'{current_num}{previous_letter}'

print(runLengthEncoding('AAAAAAAAAAAAAAAAABBBBDDDDDFGGGGRREEEEWWWWWW'))
