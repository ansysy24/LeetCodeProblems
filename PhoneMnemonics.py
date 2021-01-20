def phoneNumberMnemonics(phoneNumber):
	mnem = []
	helper(phoneNumber, mnem, '')
	return mnem

def helper(phoneNumber, mnem, current):
	if not phoneNumber:
		mnem.append(current)
	else:
		dct = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
		if phoneNumber[0] in ['0', '1']:
			helper(phoneNumber[1:], mnem, current + phoneNumber[0])
		else:
			for letter in dct[int(phoneNumber[0])]:
				helper(phoneNumber[1:], mnem, current + letter)

print(phoneNumberMnemonics('145'))
