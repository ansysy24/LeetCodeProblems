class Solution:
    def spiralOrder(self, array: List[List[int]]) -> List[int]:
        if len(array)  == 1:
            return array[0]
        elif len(array[0]) == 1:
            return [arr[0] for arr in array]

        i = 0
        j = -1
        visited = set()
        traverse = []
        while (i, j+1) not in visited:

            while j+1 < len(array[0]) and (i,j+1) not in visited:
                j += 1
                visited.add((i, j))
                traverse.append(array[i][j])

            while i+1 < len(array) and (i+1, j) not in visited:
                i += 1
                visited.add((i, j))
                traverse.append(array[i][j])

            while j-1 > -1 and (i, j-1) not in visited:
                j -= 1
                visited.add((i, j))
                traverse.append(array[i][j])

            while i-1 > -1 and (i-1, j) not in visited:
                i -= 1
                visited.add((i, j))
                traverse.append(array[i][j])

        return traverse