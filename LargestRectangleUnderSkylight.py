def largestRectangleUnderSkyline(buildings):
    max_area = 0
    for i, ht in enumerate(buildings):
        max_area = max(max_area, ht)
        start = i - 1
        end = i + 1
        cur_ht = ht
        while start > -1 or end < len(buildings):
            start = 0 if start == -1 else start
            end = len(buildings) - 1 if end == len(buildings) else end

            cur_ht = min(buildings[start], cur_ht, buildings[end])
            max_area = max(max_area, (end - start + 1) * cur_ht)

            start -= 1
            end += 1

    return max_area