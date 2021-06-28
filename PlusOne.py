class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1
        while carry and i > -1:
            carry = (digits[i] + 1)//10
            digits[i] = (digits[i] + 1)%10
            i -= 1
        return digits if not carry else [1] + digits