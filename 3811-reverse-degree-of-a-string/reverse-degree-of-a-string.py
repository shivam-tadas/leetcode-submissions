class Solution:
    def reverseDegree(self, s: str) -> int:
        ans, idx = 0, 1
        for c in s:
            ans += (123 - ord(c)) * idx
            idx += 1

        return ans