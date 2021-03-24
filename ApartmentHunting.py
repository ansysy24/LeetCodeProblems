def apartmentHunting(blocks, reqs):
    min_dist = len(blocks) - 1
    result = -1

    for i, block in enumerate(blocks):
        cur_dist = 0
        for key in reqs:
            key_dist = len(blocks) - 1
            if not block[key]:
                for j, block2 in enumerate(blocks):
                    if block2[key]:
                        key_dist = min(key_dist, abs(i - j))
            else:
                key_dist = 0

            cur_dist = max(cur_dist, key_dist)

        if cur_dist < min_dist:
            min_dist = cur_dist
            result = i
    return result