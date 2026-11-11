class Solution {
    public int minCostClimbingStairs(int[] cost) {
        ArrayList<Integer> dp = new ArrayList<>();
        int n = cost.length+1, i;
        for (i = 0; i < n+1; ++i)
            dp.add(0);
        
        for (i = n-2; i > -1; --i)
            dp.set(i, cost[i] + Math.min(dp.get(i+1), dp.get(i+2)));

        // System.out.println(dp);
        
        return Math.min(dp.get(0), dp.get(1));
    }
}