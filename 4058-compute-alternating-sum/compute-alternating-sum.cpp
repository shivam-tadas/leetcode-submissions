class Solution {
public:
    int alternatingSum(vector<int>& nums) {
        bool operation;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i % 2) operation = false;   // odd index
            else operation = true;  // even index

            if (operation) sum += nums[i];
            else sum -= nums[i];
        }
        
        return sum;
    }
};