class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_dct = self.trie
        for letter in word:
            if letter not in cur_dct:
                cur_dct[letter] = {}
            cur_dct = cur_dct[letter]
        cur_dct['#'] = '_'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_dct = self.trie
        for letter in word:
            if letter not in cur_dct:
                return False
            cur_dct = cur_dct[letter]
        return '#' in cur_dct

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_dct = self.trie
        for letter in prefix:
            if letter not in cur_dct:
                return False
            cur_dct = cur_dct[letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)