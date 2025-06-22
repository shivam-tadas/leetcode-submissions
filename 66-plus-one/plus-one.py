class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 10:
            digits[-1] += 1
        elif len(digits) > 1:
            digits[-1] = 0
            digits[-2] += 1

        for i in range(len(digits) - 1, 0, -1):
            if digits[i] > 9:
                digits[i] -= 10
                digits[i-1] += 1    # Perform carry operation

        if digits[0] > 9:
            digits[0] -= 10
            digits = [1] + digits   # Add final carry

        return digits