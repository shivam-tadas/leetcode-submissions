class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> occurence = new HashMap<>();
        int ans[] = new int[1];
        boolean hasOdd[] = { false };
        for (int i = 0; i < s.length(); ++i)
            occurence.put(s.charAt(i), occurence.getOrDefault(s.charAt(i), 0) + 1);
        
        occurence.forEach((c, freq) -> {
            if (freq % 2 == 1) {
                hasOdd[0] = true;
                ans[0] += freq-1;
            } else ans[0] += freq;

        });

        if (hasOdd[0]) return ans[0] + 1;
        
        return ans[0];
    }
}