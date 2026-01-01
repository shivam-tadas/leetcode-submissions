class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n-1
        digits[i] += 1
        carry = False
        while i >= 0:
            if carry:
                digits[i] += 1
                carry = False
            if digits[i] >= 10:
                carry = True
                digits[i] %= 10

            i -= 1

        if carry:
            carry = False
            digits.insert(0, 1)

        return digits