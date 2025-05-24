class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        subarrays = 0

        for i in range(n-2):    # Check condition for every possible subarray
            if nums[i] + nums[i+2] == nums[i+1] / 2:
                subarrays += 1

        return subarrays