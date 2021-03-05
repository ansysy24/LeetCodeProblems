def maxProfitWithKTransactions(prices, k):
    if len(prices) < 2:
        return 0
    while prices[0] == prices[1]:
        prices.pop(0)
    if len(prices) < 2:
        return 0
    while prices[-1] == prices[-2]:
        prices.pop()
    if len(prices) < 2:
        return 0

    peaks = []
    final_peak = ()
    if prices[1] > prices[0]:
        peaks.append(("mn", prices[0]))
    elif prices[1] < prices[0]:
        peaks.append(("mx", prices[0]))

    if prices[-1] > prices[-2]:
        final_peak = ("mx", prices[-1])
    elif prices[-1] < prices[-2]:
        final_peak = ("mn", prices[-1])

    for i in range(1, len(prices) - 1):
        if prices[i - 1] <= prices[i] > prices[i + 1]:
            peaks.append(("mx", prices[i]))

        elif prices[i - 1] >= prices[i] < prices[i + 1]:
            peaks.append(("mn", prices[i]))

    peaks.append(final_peak)

    while peaks and peaks[0][0] == "mx":
        peaks.pop(0)

    while peaks and peaks[-1][0] == "mn":
        peaks.pop()

    if len(peaks) < 2:
        return 0

    profit = 0

    if k < profit / 2:
        pass

    while k and peaks:
        profit -= peaks[0][1]
        peaks.pop(0)
        profit += peaks[0][1]
        peaks.pop(0)
        k -= 1

    return profit