class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = [-1 for _ in range(len(arr))]

        for i in range(len(arr) - 1):
            answer[i] = max(arr[i + 1:])

        return answer