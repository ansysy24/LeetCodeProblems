class Solution:
    def toLowerCase(self, s: str) -> str:
        to_lower = ord('a') - ord('A')
        start_upper = ord('A')
        end_upper = ord('Z')
        output = ''
        for letter in s:
            number = ord(letter)
            if start_upper <= number <= end_upper:
                letter = chr(number + to_lower)

            output += letter

        return output