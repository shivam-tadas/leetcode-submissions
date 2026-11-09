class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length, l, r, curr, ans;
        Arrays.sort(nums);
        ans = nums[n-1] + nums[n-2] + nums[n-3];
        curr = ans - target;
        for (int fix = 0; fix < n - 2; ++fix) {
            l = fix + 1;
            r = n - 1;
            while (l < r) {
                curr = nums[fix] + nums[l] + nums[r];
                if (Math.abs(curr - target) < Math.abs(ans - target))
                    ans = curr;
                if (curr == target) break;
                if (curr < target) l += 1;
                else r -= 1;
            }
            if (ans == target) break;
        }
        return ans;
    }
}