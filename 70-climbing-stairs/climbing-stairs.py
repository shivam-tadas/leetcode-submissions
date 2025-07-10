class Solution(object):
    def climbStairs(self, n):
        self.memo = {}
        return self.climbStairsHelper(n)

    def climbStairsHelper(self, n):
        if n == 0:
            return 1

        if n < 0:
            return 0

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.climbStairsHelper(n-1) + self.climbStairsHelper(n-2)
        return self.memo[n]