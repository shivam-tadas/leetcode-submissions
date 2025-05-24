class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, reach, steps = 0, 0, 0

        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])
            if i == steps:
                jumps += 1
                steps = reach

        return jumps