class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        runningSum = 0
        leftSum = []
        for i in nums:
            leftSum.append(runningSum)
            runningSum += i

        runningSum = 0
        rightSum = []
        for i in range(n - 1, -1, -1):
            rightSum.insert(0, runningSum)
            runningSum += nums[i]

        ans = []
        for i in range(n):
            ans.append(abs(leftSum[i] - rightSum[i]))

        return ans