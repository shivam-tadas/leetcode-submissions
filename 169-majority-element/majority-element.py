class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        
        max_freq = 0
        ans = 0
        for i in nums_dict:
            if nums_dict[i] > max_freq:
                ans = i
                max_freq = nums_dict[i]

        return ans