class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        letters_count = 0
        for char in s:
            letters_count += 0 if char == '-' else 1

        if not letters_count:
            return ''

        first_len = letters_count % k
        group_len = k

        result = ''

        i = 0
        while first_len:
            if s[i] != '-':
                result += s[i].upper()
                first_len -= 1
            i += 1
        result += '-' if letters_count % k else ''

        current_group = 0
        while i < len(s):
            if current_group == group_len:
                result += '-'
                current_group = 0

            if s[i] != '-':
                result += s[i].upper()
                current_group += 1

            i += 1

        return result if result[-1] != '-' else result[:-1]