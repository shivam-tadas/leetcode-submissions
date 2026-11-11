class Solution {
    public int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 1;

        ArrayList<Integer> trib = new ArrayList<>();
        trib.add(0);
        trib.add(1);
        trib.add(1);
        
        for (int i = 3; i <= n; ++i)
            trib.add(trib.get(i-3) + trib.get(i-2) + trib.get(i-1));
        
        return trib.get(n);
    }
}