class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.n = len(nums)
        self.subsets = []
        self.subsets2([], 0)
        return self.subsets

    def subsets2(self, curr: List[int], start: int):
        if curr not in self.subsets:
            self.subsets.append(curr)
            
        if start == self.n:
            return

        for i in range(start, self.n):
            self.subsets2(curr + [self.nums[i]], i+1)