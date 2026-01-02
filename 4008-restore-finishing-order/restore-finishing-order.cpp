class Solution {
public:
    vector<int> recoverOrder(vector<int>& order, vector<int>& friends) {
        vector<int> ans;
        for (int i: order) {
            for (int j = 0; j < friends.size(); j++) {
                if (i == friends[j]) {
                    ans.push_back(i);
                    break;
                }
            }
        }
        return ans;
    }
};