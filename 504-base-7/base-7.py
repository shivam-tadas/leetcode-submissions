class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
            
        ans = ''
        negative_sign = False
        if num < 0:
            negative_sign = True
            num = -num

        while num:
            ans = str(num % 7) + ans
            num //= 7
        
        if negative_sign:
            ans = '-' + ans

        return ans