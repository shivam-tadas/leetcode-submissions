class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profits = [0 for _ in range(len(prices))]
        print(profits)

        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
                profits[i] = 0
                continue

            profits[i] = prices[i] - minPrice

        print(profits)
        return max(profits)