def firstNonRepeatingCharacter(string):
    indexes = {}

    for letter in string:
        indexes[letter] = indexes.get(letter, 0) + 1

    for i, letter in enumerate(string):
        if indexes[letter] == 1:
            return i

    return -1