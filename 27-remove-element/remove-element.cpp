class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int sz = nums.size();
        
        for (int i = 0; i < sz; i++)
            if (nums[i] == val) {   // If val is found at a position i
                sz--;    // Shrink "size" of array by 1
                for (int j = i; j < nums.size() - 1; j++)
                    nums[j] = nums[j + 1];  // Delete element at i by copying elements ahead
                i--;
            }

        return sz;
    }
};