class Solution:
    def checkRecord(self, s: str) -> bool:
        a_counter = 0
        l_counter = 0
        for char in s:
            if char == 'A':
                a_counter += 1
                l_counter = 0
                if a_counter == 2:
                    return False
            else:
                if char == 'L':
                    l_counter += 1
                    if l_counter == 3:
                        return False
                else:
                    l_counter = 0
        return True
