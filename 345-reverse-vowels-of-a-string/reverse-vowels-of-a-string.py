class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        n = len(s)
        left = 0
        right = n-1
        s_list = list(s)
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1

            while right > left and s[right] not in vowels:
                right -= 1

            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        s = "".join(s_list)
        return s