def laptopRentals(times):
    times.sort()
    if not times:
        return 0
    ends = [times[0][1]]
    times.pop(0)
    max_laptops = 1

    for time in times:
        if time[0] >= ends[0]:
            while ends and ends[0] <= time[0]:
                ends.pop(0)

        ends.append(time[1])
        ends.sort()
        max_laptops = max(max_laptops, len(ends))

    return max_laptops