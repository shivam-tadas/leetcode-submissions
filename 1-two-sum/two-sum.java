class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i, n = nums.length;
        int ans[] = new int[2];
        Map<Integer, Integer> indices = new HashMap<>();
        for (i = 0; i < n; i++)
            indices.put(nums[i], i);
        
        for (i = 0; i < n; i++) {
            if (indices.containsKey(target-nums[i]) && indices.get(target-nums[i]) != i) {
                ans[0] = i;
                ans[1] = indices.get(target-nums[i]);
                return ans;
            }
        }

        return ans;
    }
}