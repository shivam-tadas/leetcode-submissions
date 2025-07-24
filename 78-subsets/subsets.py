class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.n = len(nums)
        self.subsets = []
        self.subsetsHelper([], -1)
        return self.subsets

    def subsetsHelper(self, curr: List[int], start: int) -> None:
        self.subsets.append(curr)

        if start > self.n:
            return

        for i in range(start+1, self.n):
            self.subsetsHelper(curr + [self.nums[i]], i)