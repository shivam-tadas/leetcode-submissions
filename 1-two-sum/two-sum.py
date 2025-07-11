class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        map = {}

        for i in range(n):
            rem = target - nums[i]
            if(rem in map):
                return [map[rem], i]
            map[nums[i]] = i
            