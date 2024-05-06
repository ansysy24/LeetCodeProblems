# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    one = []
    two = []
    while descendantOne is not None:
        one.append(descendantOne)
        descendantOne = descendantOne.ancestor

    while descendantTwo is not None:
        two.append(descendantTwo)
        descendantTwo = descendantTwo.ancestor

    youngest = None
    print([n.name for n in one], [n.name for n in two])
    for i in range(-1, -min(len(one), len(two)) - 1, -1):
        if one[i] == two[i]:
            youngest = one[i]

    return youngest
