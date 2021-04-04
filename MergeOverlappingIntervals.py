def mergeOverlappingIntervals(intervals):
    result = []
    intervals.sort()
    while intervals:
        current = intervals.pop(0)
        mx = current[1]

        while intervals and intervals[0][0] <= mx:
            mx = max(mx, intervals[0][1])
            intervals.pop(0)

        result.append([current[0], mx])

    return result