class Solution:
    def reverseBits(self, n: int) -> int:
        i = 0
        ans = 0

        while i < 32:
            ans *= 2
            ans += n % 2
            n //= 2
            i += 1

        return ans