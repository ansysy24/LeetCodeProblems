def minimumCharactersForWords(words):
    dct = {}
    for word in words:
        curr_dct = {}
        for letter in word:
            curr_dct[letter] = curr_dct.get(letter, 0) + 1

        for key in curr_dct:
            dct[key] = max(dct.get(key, 0), curr_dct[key])


    answer = []
    for key in dct:
        answer += [key] * dct[key]

    return answer