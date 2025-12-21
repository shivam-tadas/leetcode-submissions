class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split('+')
        num2 = num2.split('+')
        r1 = int(num1[0])
        r2 = int(num2[0])
        i1 = int(num1[1][0:-1])
        i2 = int(num2[1][0:-1])
        print(r1, r2, i1, i2)
        r_a = r1 * r2 - i1 * i2
        i_a = r1 * i2 + r2 * i1
        return str(r_a) + '+' + str(i_a) + 'i'