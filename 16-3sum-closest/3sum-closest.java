class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length, i, j, k, minDiff = 99999, ans = 0;
        for (i = 0; i < n-2; ++i)
            for (j = i+1; j < n-1; ++j)
                for (k = j+1; k < n; ++k)
                    if (Math.abs(nums[i]+nums[j]+nums[k]-target) < minDiff) {
                        minDiff = Math.abs(nums[i]+nums[j]+nums[k]-target);
                        ans = nums[i] + nums[j] + nums[k];
                    }
        return ans;
    }
}