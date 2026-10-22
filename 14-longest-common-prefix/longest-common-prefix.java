class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder ans = new StringBuilder();
        int minLength = Arrays.stream(strs).mapToInt(String::length).min().orElse(0), i = 0;
        boolean flag = false;
        while (i < minLength) {
            char curr = strs[0].charAt(i);
            for (String s: strs) {
                if (s.charAt(i) != curr) {
                    flag = true;
                    break;
                }
            }
            if (flag) break;
            i++;
            ans.append(curr);
        }
        return ans.toString();
    }
}