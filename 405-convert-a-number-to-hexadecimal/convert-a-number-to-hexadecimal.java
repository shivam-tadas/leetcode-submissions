class Solution {
    public String toHex(int num) {
        int i, tmp;
        Map<Integer, Character> digits = new HashMap<>();
        StringBuilder ans = new StringBuilder();

        digits.put(0, '0');
        digits.put(1, '1');
        digits.put(2, '2');
        digits.put(3, '3');
        digits.put(4, '4');
        digits.put(5, '5');
        digits.put(6, '6');
        digits.put(7, '7');
        digits.put(8, '8');
        digits.put(9, '9');
        digits.put(10, 'a');
        digits.put(11, 'b');
        digits.put(12, 'c');
        digits.put(13, 'd');
        digits.put(14, 'e');
        digits.put(15, 'f');

        for (i = 0; i < 8; ++i) {
            tmp = (num >> (i * 4)) & 15;    // Shift and extract last 4 digits by iteration
            System.out.println(tmp);
            ans.append(digits.get(tmp));
            System.out.println(ans);
        }
        ans.reverse();
        while (ans.length() > 1 && ans.charAt(0) == '0')
            ans = new StringBuilder(ans.substring(1));

        return ans.toString();
    }
}