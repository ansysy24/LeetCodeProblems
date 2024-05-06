class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        result = 0
        for word in text.split():
            include = True
            for letter in word:
                if letter in broken:
                    include = False
                    break
            if include:
                result += 1

        return result
