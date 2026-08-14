class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        i = 0
        while i < 32:
            ans *= 2
            ans += n % 2
            n //= 2
            i += 1

        return ans