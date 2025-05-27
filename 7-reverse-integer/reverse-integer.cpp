class Solution {
public:
    int reverse(int x) {
        long int x2 = (long int)x, reverse = 0;
        
        if (x2 >= 0) {  // If number is positive
            while (x2 != 0) {
                reverse *= 10;
                reverse += x2 % 10;
                x2 /= 10;
            }
        }
        else {
            x2 *= -1;   // When number is negative

            while (x2 != 0) {
                reverse *= 10;
                reverse += x2 % 10;
                x2 /= 10;
            }

            reverse *= -1;
        }

        return reverse == (int)reverse ? reverse : 0;
    }
};