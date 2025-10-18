class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> nMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (nMap.containsKey(complement)) {
                int ans[] = {nMap.get(complement), i};
                return ans;
            }
            nMap.put(nums[i], i);
        }
        int ans[] = {0, 0};
        return ans;
    }
}