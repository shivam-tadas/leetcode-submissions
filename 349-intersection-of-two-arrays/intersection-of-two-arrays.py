class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    common.add(i)

        return list(common)