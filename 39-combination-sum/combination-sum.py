class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target
        self.curr = []
        self.cSum = 0
        self.maxCurr = -1
        self.combinations = []

        self.combinationSumHelper()
        return self.combinations

    def combinationSumHelper(self) -> None:
        if self.cSum >= self.target:
            if self.cSum == self.target:
                self.combinations.append(self.curr.copy())
            return

        i = 0
        while i < len(self.candidates):
            if self.candidates[i] >= self.maxCurr:
                tmp = self.maxCurr
                self.maxCurr = self.candidates[i]
                self.cSum += self.candidates[i]
                self.curr.append(self.candidates[i])
                self.combinationSumHelper()
                self.curr.pop()
                self.cSum -= self.candidates[i]
                self.maxCurr = tmp  # Backtrack to previous state
                
            i += 1