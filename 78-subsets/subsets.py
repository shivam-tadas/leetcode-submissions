class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.numsSubsets = []
        self.nums = nums
        self.n = len(nums)
        self.subsetsHelper([], 0)

        return self.numsSubsets

    def subsetsHelper(self, currset:List[int], start: int) -> None:
        self.numsSubsets.append(currset.copy())

        for i in range(start, self.n):
            self.subsetsHelper(currset + [self.nums[i]], i + 1)