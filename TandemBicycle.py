def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.reverse()


    return sum([max(pair) for pair in zip(blueShirtSpeeds, redShirtSpeeds)])