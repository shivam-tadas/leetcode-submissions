class Solution:
    def reverseBits(self, n: int) -> int:
        i = 0
        ans = 0
        negative = False

        if n < 0:
            n *= -1
            negative = True

        while i < 32:
            ans *= 2
            ans += n % 2
            n //= 2
            i += 1

        if negative:
            ans *= -1

        return ans