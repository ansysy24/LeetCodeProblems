class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        current_word = ''
        for char in s:
            if char != ' ':
                current_word = char + current_word
            else:
                result += current_word + ' '
                current_word = ''

        return result[:-1] if not current_word else result + current_word