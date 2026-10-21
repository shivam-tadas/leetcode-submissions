class Solution {
    public double myPow(double x, int n) {
        if (n == 0) return 1;
        if (x == 1.0) return x;
        if (n == 1) return x;
        if (x == -1 && n%2 == 1) return -1;
        if (x == -1 && n%2 == 0) return 1;
        if (n == -2147483648) return 0.0;

        if (n < 0) return 1 / (myPowHelper(x, -n));
        return myPowHelper(x, n);
    }

    private static double myPowHelper(double x, int n) {
        if (n == 0) return 1;
        if (n == 1) return x;

        double p1;
        if (n%2 == 1) {
            p1 = myPowHelper(x, n/2);
            return p1 * p1 * x;
        }
        
        p1 = myPowHelper(x, n/2);
        return p1 * p1;
    }
}