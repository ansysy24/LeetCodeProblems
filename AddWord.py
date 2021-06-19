class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        current_trie = self.trie
        for letter in word:
            if letter not in current_trie:
                current_trie[letter] = {}
            current_trie = current_trie[letter]

        current_trie['*'] = {}

    def search(self, word: str, current_trie=None) -> bool:
        if current_trie is None:
            current_trie = self.trie
        for i, letter in enumerate(word):
            if letter == '.':
                for key in current_trie:
                    if key == '*':
                        continue

                    if self.search(word[i + 1:], current_trie[key]):
                        return True

                return False

            elif letter not in current_trie:
                return False
            current_trie = current_trie[letter]
        return '*' in current_trie