class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5: return 0

        zeroes = 0

        while n >= 5:
            n //= 5
            zeroes += n

        return zeroes