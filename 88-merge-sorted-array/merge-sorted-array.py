class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return

        n1p, n2p, wp = m-1, n-1, m+n-1
        while n2p >= 0:
            if n1p >= 0 and nums1[n1p] > nums2[n2p]:
                nums1[wp] = nums1[n1p]
                wp -= 1
                n1p -= 1
            else:
                nums1[wp] = nums2[n2p]
                wp -= 1
                n2p -= 1