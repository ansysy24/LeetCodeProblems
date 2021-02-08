class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        array.append(self.name)
        level = [self]
        while level:
            next_level = []
            for n in level:
                for ch in n.children:
                    array.append(ch.name)
                    next_level.append(ch)
            level = next_level
        return array