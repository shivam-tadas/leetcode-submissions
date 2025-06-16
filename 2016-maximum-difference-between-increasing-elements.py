class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = []
        prefixMin = []
        tmpMin = nums[0]

        for i in range(n):
            if nums[i] < tmpMin:
                tmpMin = nums[i]

            prefixMin.append(tmpMin)

        for i in range(n - 1):
            if prefixMin[i] <= nums[i]:
                maxDiff = -1
                for j in range(i + 1, n):
                    diff = nums[j] - nums[i]
                    if diff > 0 and diff > maxDiff:
                        maxDiff = diff

                diffs.append(maxDiff)
                print(diffs)

        return max(diffs) if diffs else -1
