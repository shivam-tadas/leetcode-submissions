class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        char nextGreatest = '0';
        
        for (int i = 0; i < letters.size(); i++) {
            if (letters[i] > target) {
                nextGreatest = letters[i];
                break;
            }
        }

        if (nextGreatest == '0') {
            return letters[0];
        }
        
        return nextGreatest;
    }
};