class Solution {
    List<List<Integer>> permutations;
    List<Integer> nums;

    public List<List<Integer>> permute(int[] nums) {
        permutations = new ArrayList<>();
        this.nums = new ArrayList<>();
        for (int i: nums) {
            this.nums.add(i);   // Create arraylist from array
        }
        List<Integer> current = new ArrayList<>();
        permuteHelper(current);
        return permutations;
    }

    public void permuteHelper(List<Integer> curr) {
        if (nums.size() == 0) {
            permutations.add(new ArrayList<>(curr));
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            int x = nums.remove(i);
            curr.add(x);
            permuteHelper(curr);
            curr.remove(curr.size()-1);
            nums.add(i, x);
        }
    }
}