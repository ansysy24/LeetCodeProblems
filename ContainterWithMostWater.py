class Solution:
    def maxArea(self, height: List[int]) -> int:

        h = list(enumerate(height))
        mx = 0
        for i in range(len(h) - 1):
            for j in range(i + 1, len(h)):
                h1 = h[i]
                h2 = h[j]
                water = abs(h1[0] - h2[0]) * min(h1[1], h2[1])
                mx = max(mx, water)

        return mx