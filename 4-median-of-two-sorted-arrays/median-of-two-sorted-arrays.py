class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n == 1:
            return merged[0]

        mid = n//2
        if n % 2:
            return merged[mid]
        
        return (merged[mid-1] + merged[mid]) / 2
        