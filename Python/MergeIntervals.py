class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        while intervals:
            current = intervals.pop(0)
            i = 0
            while i < len(intervals):
                if current[1] >= intervals[i][0] and current[1] < intervals[i][1]:
                    change = intervals.pop(i)
                    current[1] = change[1]
                    current[0] = min(change[0], current[0])

                elif current[0] <= intervals[i][1] and current[0] > intervals[i][0]:
                    change = intervals.pop(i)
                    current[0] = change[0]
                    current[1] = max(change[1], current[1])

                elif current[0] <= intervals[i][0] and current[1] >= intervals[i][1]:
                    intervals.pop(i)

                else:
                    i += 1

            output += [current]

        return output