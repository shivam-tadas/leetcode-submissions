class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1.0;
        if (n == 1) return x;

        long long N = n;

        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        return myPowHelper(x, N);
    }

private:
    double myPowHelper(double x, long long n) {
        if (n == 0) return 1.0;

        double half = myPowHelper(x, n / 2);

        if (n % 2 == 0) {
            return half * half; // When power is even
        }
        return half * half * x; // When power is odd
    }
};