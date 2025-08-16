class Solution {
public:
    int maximum69Number (int num) {
        vector<int> digits;
        while (num) {
            digits.push_back(num%10);
            num /= 10;
        }
        reverse(digits.begin(), digits.end());

        // for (int i=0; i < digits.size(); i++)
        //     cout << digits[i] << ' ';
        // cout << endl;

        for (int i=0; i < digits.size(); i++) {
            if (digits[i] == 6) {
                digits[i] = 9;
                break;
            }
        }

        int newNum = 0;
        for (int i: digits) {
            newNum *= 10;
            newNum += i;
        }

        return newNum;
    }
};