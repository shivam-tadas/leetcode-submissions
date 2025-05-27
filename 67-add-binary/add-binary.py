class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Make the number of digits in both numbers equal
        if len(a) > len(b):
            while len(b) != len(a):
                b = '0' + b

        elif len(b) > len(a):
            while len(a) != len(b):
                a = '0' + a

        print(a, b)

        # Add digit by digit, from right to left
        carry = '0'
        ans = ''

        for i in range(len(a) - 1, -1, -1):
            if a[i] == '1' and b[i] == '1':
                if carry == '0':
                    ans = '0' + ans
                    carry = '1'
                else:
                    ans = '1' + ans

            elif (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1'):
                if carry == '0':
                    ans = '1' + ans
                else:
                    ans = '0' + ans     # Carry will remain as it is

            elif a[i] == '0' and b[i] == '0':
                ans = carry + ans
                carry = '0'

        if carry == '1':
            ans = '1' + ans

        return ans