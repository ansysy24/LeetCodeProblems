def generateDocument(characters, document):
    dct = {}
    for char in characters:
        dct[char] = dct.get(char, 0) + 1

    for char in document:
        if char in dct:
            if not dct[char]:
                return False
            else:
                dct[char] -= 1
        else:
            return False

    return True