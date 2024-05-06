def generateDivTags(numberOfTags):
    ways = []
    helper(numberOfTags, numberOfTags, ways, '')
    return ways

def helper(opening, closing, ways, current_way):
    if not opening:
        ways.append(current_way + '</div>' * closing)
    elif opening == closing:
        helper(opening-1, closing, ways, current_way + '<div>')
    else:
        helper(opening-1, closing, ways, current_way + '<div>')
        helper(opening, closing-1, ways, current_way + '</div>')