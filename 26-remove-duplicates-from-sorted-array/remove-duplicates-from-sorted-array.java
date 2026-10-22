class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 1) return 1;

        int ptr1 = 0, ptr2 = 1;
        while (ptr2 < nums.length) {
            if (nums[ptr1] != nums[ptr2]) {
                ++ptr1;
                ++ptr2;
            } else {
                while (ptr2 < nums.length && nums[ptr2] == nums[ptr1])
                    ++ptr2;
                if (ptr2 == nums.length) break;
                nums[++ptr1] = nums[ptr2];
            }
        }
        return ++ptr1;
    }
}