class Solution:
    set_list = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

    def findWords(self, words: List[str]) -> List[str]:
        one_row_words = []
        for word in words:
            for set_ in self.set_list:
                if set(word.lower()).issubset(set_):
                    one_row_words.append(word)
                    break

        return one_row_words