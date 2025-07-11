class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nmap = {}

        for i in range(n):
            if target-nums[i] in nmap:
                return [nmap[target-nums[i]], i]
            nmap[nums[i]] = i