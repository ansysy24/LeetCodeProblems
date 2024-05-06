def ambiguousMeasurements(measuringCups, low, high):
    measuringCups.sort()
    memo = {}

    for meas in measuringCups:
        if meas[0] > low or meas[1] > high:
            break
        if helper(measuringCups, low - meas[0], high - meas[1], high - low, memo):
            return True
        return False


def helper(measuringCups, low, high, diff, memo):
    print(low, high)
    for meas in measuringCups:
        if meas[0] > low or meas[1] > high:
            if high - low <= diff:
                return True
        else:
            memo[(low, high)] = memo.get((low, high), helper(measuringCups, low - meas[0], high - meas[1], diff, memo))

    return False