class Solution:
    def isHappy(self, n: int) -> bool:        
        n_orig = n

        while n > 3:
            tmpSum = 0  # Store sum of squares of digits of n

            while n != 0:
                tmp = n % 10
                n //= 10
                tmpSum += tmp ** 2

            n = tmpSum

            if n == n_orig or n == 4:
                return False    # If the process loops
        
        if n == 1:
            return True
        
        return False