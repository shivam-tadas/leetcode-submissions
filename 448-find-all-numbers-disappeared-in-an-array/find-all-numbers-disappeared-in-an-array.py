class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        disappeared = []
        num_dict = {}
        for i in range(1, n+1):
            num_dict[i] = 0

        for i in nums:
            num_dict[i] += 1

        for i in range(1, n+1):
            if num_dict[i] == 0:
                disappeared.append(i)
                
        return disappeared