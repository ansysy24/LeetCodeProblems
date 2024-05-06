class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_max = []


    def peek(self):
        return self.stack[-1] if self.stack else None


    def pop(self):
        self.min_max.pop()
        pop = self.stack.pop() if self.stack else None
        return pop


    def push(self, number):
        self.stack.append(number)
        if self.min_max:
            self.min_max.append((min(number, self.min_max[-1][0]), max(number, self.min_max[-1][1])))
        else:
            self.min_max = [(number, number)]


    def getMin(self):
        return self.min_max[-1][0] if self.min_max else None


    def getMax(self):
        return self.min_max[-1][1] if self.min_max else None