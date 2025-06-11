class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = [False for _ in range(n)]
        reach[-1] = True

        for i in range(n-2, -1, -1):
            for j in range(i+1, min(n, i+nums[i]+1)):
                if reach[j] == True:
                    reach[i] = True
                    break

        return reach[0]