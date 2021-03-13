class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        elif len(b) > len(a):
            a = '0' * (len(b) - len(a)) + a

        output = ''
        index = -1
        carry = 0
        while index >= -len(a):
            output = str((int(a[index]) + int(b[index]) + carry) % 2) + output
            carry = int((int(a[index]) + int(b[index]) + carry) // 2)
            index -= 1

        if carry:
            output = '1' + output

        return output