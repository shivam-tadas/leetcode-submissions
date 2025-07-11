class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.target = target
        self.combinations = []

        self.cs2Helper([], -1, 0)
        return self.combinations

    def cs2Helper(self, path: List[int], start: int, pathSum: int) -> None:
        if pathSum >= self.target:
            if (pathSum == self.target) and (path not in self.combinations):
                self.combinations.append(path)

            return

        i = start + 1
        while i < len(self.candidates):
            if not (i > start + 1 and self.candidates[i] == self.candidates[i - 1]):
                self.cs2Helper(path + [self.candidates[i]], i, pathSum + self.candidates[i])
            i += 1