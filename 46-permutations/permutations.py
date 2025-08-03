class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []

        if len(nums) == 1:  # If list has only one element
            return [nums]

        self.permutations = []
        self.permuteHelper(nums, [])
        return self.permutations

    def permuteHelper(self, nums: List[int], permutation: List[int]) -> None:
        if nums == []:
            self.permutations.append(permutation.copy())
            return
        
        for i in range(len(nums)):
            x = nums.pop(i)
            self.permuteHelper(nums, permutation+[x])
            nums.insert(i, x)