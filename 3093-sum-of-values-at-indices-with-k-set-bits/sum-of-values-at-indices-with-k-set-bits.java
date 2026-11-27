class Solution {
    public int sumIndicesWithKSetBits(List<Integer> nums, int k) {
        int n = nums.size();
        int[] setBits = new int[n];
        setBits[0] = 0;
        if (n > 1) {
            setBits[1] = 1;
            for (int i = 2; i < n; ++i)
                setBits[i] = setBits[i>>1] + i%2;
        }
        int ans = 0;
        for (int i = 0; i < n; ++i)
            if (setBits[i] == k) {
                System.out.println(nums.get(i));
                ans += nums.get(i);
            }
        
        return ans;
    }
}