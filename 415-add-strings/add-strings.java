class Solution {
    public String addStrings(String num1, String num2) {
        int n1Size = num1.length(), n2Size = num2.length(), digits, digitPos = 1;
        digits = Math.max(n1Size, n2Size);
        boolean carry = false;
        StringBuilder ans = new StringBuilder();
        while (digitPos <= digits) {
            char sumDigit = '0';
            if (digitPos > n1Size) {
                sumDigit = (char)(num2.charAt(n2Size-digitPos));
                if (carry) {
                    ++sumDigit;
                    carry = false;
                }
            } else if (digitPos > n2Size) {
                sumDigit = (char)(num1.charAt(n1Size-digitPos));
                if (carry) {
                    ++sumDigit;
                    carry = false;
                }
            } else {
                sumDigit = (char)(num1.charAt(n1Size-digitPos) + num2.charAt(n2Size-digitPos) - '0');
                if (carry) {
                    ++sumDigit;
                    carry = false;    
                } 
            }

            if (sumDigit <= '9')
                ans.insert(0, sumDigit);
            else {
                ans.insert(0, (char)(sumDigit - 10));
                carry = true;
            }
            ++digitPos;
        }
        if (carry) ans.insert(0, '1');
        
        return ans.toString();
    }
}