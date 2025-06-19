class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        partitions = 0
        i = 0

        while i < n:
            lowEle = nums[i]
            while i < n and nums[i] <= lowEle + k:
                i += 1

            partitions += 1

        return partitions