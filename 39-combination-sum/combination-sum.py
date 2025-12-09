class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []
        self.candidates = candidates
        self.target = target
        self.combinationSumHelper(0, [], 0)
        return self.combinations

    def combinationSumHelper(self, start: int, curr: List[int], cSum: int) -> None:
        if cSum > self.target:
            return

        if cSum == self.target:
            self.combinations.append(curr)
            return
        
        for i in range(start, len(self.candidates)):
            self.combinationSumHelper(i, curr + [self.candidates[i]], cSum + self.candidates[i])
