class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        set_al = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z'])
        set_1 = set(sentence)
        return set_al == set_1