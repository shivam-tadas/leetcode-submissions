class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Dict = {}
        nums2Dict = {}
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums1Dict:
                nums1Dict[nums1[i]] += 1
            else:
                nums1Dict[nums1[i]] = 1

        for i in range(len(nums2)):
            if nums2[i] in nums2Dict:
                nums2Dict[nums2[i]] += 1
            else:
                nums2Dict[nums2[i]] = 1

        print(nums1Dict, nums2Dict)
        for i in nums1Dict:
            if i in nums2Dict:
                for j in range(min(nums1Dict[i], nums2Dict[i])):
                    ans.append(i)

        return ans