def longestSubstringWithoutDuplication(string):
    dct = {}
    start = 0
    longest = 0
    longest_start = 0
    longest_end = len(string)
    for i, char in enumerate(string):
        if char in dct:
            start = max(start, dct[char] + 1)

        if i - start > longest:
            longest = i - start
            longest_start = start
            longest_end = i + 1

        dct[char] = i

    return string[longest_start: longest_end]

print(longestSubstringWithoutDuplication('klenentisakap'))

