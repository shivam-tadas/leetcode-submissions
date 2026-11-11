class Solution {
    public int fib(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        ArrayList<Integer> fib = new ArrayList<>();
        fib.add(0);
        fib.add(1);
        for (int i = 2; i < n; ++i)
            fib.add(fib.get(i-1) + fib.get(i-2));
        
        return fib.get(n-1) + fib.get(n-2);
    }
}