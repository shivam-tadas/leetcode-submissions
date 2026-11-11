class Solution {
    public int minCostClimbingStairs(int[] cost) {
        ArrayList<Integer> dp = new ArrayList<>();
        int n = cost.length+1;
        for (int i = 0; i <= n; ++i)
            dp.add(0);
        
        for (int i = n-2; i >= 0; --i)
            dp.set(i, cost[i] + Math.min(dp.get(i+1), dp.get(i+2)));

        System.out.println(dp);
        
        return Math.min(dp.get(0), dp.get(1));
    }
}