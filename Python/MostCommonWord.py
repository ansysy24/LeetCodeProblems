class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        current_word = ''
        max_word = ''
        word_dct = {}
        counter = 0
        for i, char in enumerate(paragraph):
            if char not in "!?',;. ":
                current_word += char
                if i < len(paragraph) - 1:
                    continue
            if current_word:
                current_word = current_word.lower()
                word_dct[current_word] = word_dct.get(current_word, 0) + 1
                if current_word not in banned_set and word_dct[current_word] > counter:
                    max_word = current_word
                    counter = word_dct[current_word]
                current_word = ''

        return max_word