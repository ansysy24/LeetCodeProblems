class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = 0
        i = 0
        while i + zeros < len(arr) - 1:
            zeros = zeros if arr[i] else zeros + 1
            i += 1

        i = len(arr) - 1
        while i - zeros >= 0 and zeros > 0:
            print(i, zeros)
            arr[i] = arr[i - zeros]
            if arr[i - zeros] == 0:
                arr[i - 1] = 0
                zeros -= 1
                i -= 1
            i -= 1
            print(arr)