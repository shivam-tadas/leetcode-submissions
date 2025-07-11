class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        arr = [[i, nums[i]] for i in range(len(nums))]
        arr.sort(key=lambda x:x[1])
        left, right = 0, n-1
        while left<right:
            print(arr[left][1], arr[right][1], target)
            if arr[left][1]+arr[right][1] == target:
                return [arr[left][0], arr[right][0]]

            if arr[left][1]+arr[right][1]< target:
                left += 1
            else:
                right -= 1

        return [0, 0]