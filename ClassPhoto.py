def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    smaller = None
    if redShirtHeights[0] == blueShirtHeights[0]:
        return False
    elif redShirtHeights[0] > blueShirtHeights[0]:
        smaller = blueShirtHeights
        larger = redShirtHeights
    else:
        smaller = redShirtHeights
        larger = blueShirtHeights
    for i, student in enumerate(smaller):
        if student >= larger[i]:
            return False
    return True


print(classPhotos([3, 5, 6, 8, 2, 1], [2, 4, 7, 5, 1, 6]))
