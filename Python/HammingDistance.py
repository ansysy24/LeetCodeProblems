class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x > y:
            x = bin(x)[2:]
            y = bin(y)[2:].zfill(len(x))

        else:
            y = bin(y)[2:]
            x = bin(x)[2:].zfill(len(y))

        counter = 0
        for i, char in enumerate(x):
            if char != y[i]:
                counter += 1

        return counter