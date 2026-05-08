class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 200   # largest possible length according to constraint
        for i in strs:
            min_len = min(min_len, len(i))

        break_loop = False
        ptr = 0

        while not break_loop and ptr < min_len:
            prev = strs[0][ptr]
            for s in strs:
                if s[ptr] != prev:
                    ptr -= 1
                    break_loop = True
                    break

            ptr += 1

        return strs[0][0:ptr]