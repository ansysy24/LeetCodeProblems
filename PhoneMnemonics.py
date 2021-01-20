def phoneNumberMnemonics(phoneNumber):
	mnem = []
	helper(phoneNumber, mnem, '')
    return mnem

def helper(phoneNumber, mnem, current):
	if not phoneNumber:
		mnem.append(current)
	else:
		dct = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
		for i, number in enumerate(phoneNumber):
			if number in ['0', '1']:
				helper(phoneNumber[i+1:], mnem, current + number)
			else:
				for letter in dct[int(number)]:
					helper(phoneNumber[i+1:], mnem, current + letter)
