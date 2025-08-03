class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []

        if len(nums) == 1:  # If list has only one element
            return [nums]

        permuteList = []
        self.permuteHelper(nums, [], permuteList)
        return permuteList

    def permuteHelper(self, nums: List[int], permutation: List[int], permutations: List[List[int]]) -> None:
        if nums == []:
            permutations.append(permutation.copy())
            return
        
        for i in range(len(nums)):
            x = nums.pop(i)
            self.permuteHelper(nums, permutation+[x], permutations)
            nums.insert(i, x)