class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        indices = {}
        for i in range(n):
            if nums[i] in indices and abs(indices[nums[i]] - i) <= k:
                return True
            
            indices[nums[i]] = i

        return False