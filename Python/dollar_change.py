def change(amount, denoms = [50, 25, 10, 5, 1]):
	if 0 <= amount < 5:
		return 1 
	elif amount < 0:
		return 0	
	if denoms:			
		ways = change(amount-denoms[0], denoms) + change(amount, denoms[1:])
		return ways
	else:
		return 0

print(change(100))