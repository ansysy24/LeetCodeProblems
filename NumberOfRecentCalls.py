class RecentCounter:

    def __init__(self):
        self.times = []
        self.counter = 0

    def ping(self, t: int) -> int:
        self.times.append(t)
        self.counter += 1

        past = t - 3000

        while self.times[0] < past:
            self.times.pop(0)
            self.counter = self.counter - 1 if self.counter > 0 else 0