class Solution {
public:
    int findPermutationDifference(string s, string t) {
        unordered_map<char, int> tChars;
        for (int i = 0; i < t.size(); i++) {
            tChars[t[i]] = i;
        }
        int permutationDifference = 0;
        for (int i = 0; i < s.size(); i++) {
            permutationDifference += abs(i - tChars[s[i]]);
        }
        return permutationDifference;
    }
};