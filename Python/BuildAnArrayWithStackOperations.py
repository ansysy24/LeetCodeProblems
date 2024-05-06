class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ind = 0
        result = []
        for i in range(1, target[-1]+1):
            if target[ind] == i:
                ind += 1
                result.append("Push")
            else:
                result.append("Push")
                result.append("Pop")
        return result