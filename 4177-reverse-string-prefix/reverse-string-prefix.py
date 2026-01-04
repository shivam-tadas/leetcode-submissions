class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        s_list = list(s)
        l, r = 0, k-1
        while l < r:
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1

        new_s = ""
        for i in s_list:
            new_s += i

        return new_s