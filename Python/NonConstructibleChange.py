
def nonConstructibleChange(coins):
    coins.sort()
    current_total = 0
    for coin in coins:
        if coin > current_total + 1:
            return current_total + 1
        current_total += coin
    return current_total + 1

print(nonConstructibleChange([109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]))