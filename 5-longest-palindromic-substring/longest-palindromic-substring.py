class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
    
        if n == 1:
            return s[0]

        longestPalindromic = ''

        for k in range(1, n):   # For odd length palindromes
            i = j = k   # Pointers will be spread across the string

            while i > -1 and j < n and s[i] == s[j]:
                if j - i + 1 > len(longestPalindromic):
                    longestPalindromic = s[i:j+1]

                i -= 1
                j += 1

        for k in range(1, n):   # For even length palindromes
            i = k - 1
            j = k

            while i > -1 and j < n and s[i] == s[j]:
                if j - i + 1 > len(longestPalindromic):
                    longestPalindromic = s[i:j+1]

                i -= 1
                j += 1

        return longestPalindromic