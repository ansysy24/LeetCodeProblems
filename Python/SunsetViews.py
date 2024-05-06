def sunsetViews(buildings, direction):
    if direction == "EAST":
        buildings.reverse()
    answer = []
    mx = float('-inf')
    for i, building in enumerate(buildings):
        if building > mx:
            mx = building
            j = i
            if direction == "EAST":
                j = len(buildings) - 1 - i
            answer.append(j)
    if direction == "EAST":
        answer.reverse()
    return answer


print(sunsetViews([7, 1, 7, 8, 9, 8, 7, 6, 5, 4, 2, 5], "EAST"))
