def reverseWordsInString(string):
    new_string = ''
    current_word = ''
    for i in range(len(string) - 1, -1, -1):
        if string[i] != ' ':
            current_word = string[i] + current_word
        else:
            new_string += current_word + ' '
            current_word = ''
    return new_string + current_word

print(reverseWordsInString('This is that'))