class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder ans = new StringBuilder();
        for (String word : words) {
            int weight = 0;
            for (int i = 0; i < word.length(); ++i)
                weight += weights[word.charAt(i) - 'a'];
            int letter = 25 - (weight % 26);
            ans.append((char)(letter + 'a'));
        }
        return ans.toString();
    }
}