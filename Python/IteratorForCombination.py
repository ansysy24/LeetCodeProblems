import itertools


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = [''.join(string) for string in itertools.combinations(characters, combinationLength)]
        self.index = 0

    def next(self) -> str:
        if self.index < len(self.combinations):
            combination = self.combinations[self.index]
            self.index += 1
            return combination

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)