class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        int n = nums.size(), pairs = 0, i, j;
        
        for (i = 0; i < n; i++)
            for (j = i + 1; j < n; j++)
                if (nums[i] + nums[j] < target) pairs++;

        return pairs;
    }
};