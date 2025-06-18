class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        newNums = []

        for i in range(n // 3): # Divide into arrays of size n // 3
            newNums.append(nums[3*i:3*i+3])

        for i in newNums:   # Check if condition is not being satisfied by any array
            if max(i) - min(i) > k:
                return []
                
        return newNums