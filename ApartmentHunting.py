def apartmentHunting(blocks, reqs):
    result = len(blocks) - 1

    for i, block in enumerate(blocks):
        distance = 0

        for key in block:
            cur_dist = len(blocks) - 1

            if not block[key]:
                for j, block2 in enumerate(blocks):
                    if block2[key]:
                        cur_dist = min(cur_dist, abs(i - j))

                distance = max(distance, cur_dist)

        result = min(result, distance)

    return result