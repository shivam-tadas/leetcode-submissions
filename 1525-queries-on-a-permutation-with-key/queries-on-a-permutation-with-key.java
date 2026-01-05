class Solution {
    public int[] processQueries(int[] queries, int m) {
        ArrayList<Integer> numList = new ArrayList<>();
        ArrayList<Integer> ans = new ArrayList<>();
        for (int i = 1; i <= m; i++) numList.add(i);
        for (int i = 0; i < queries.length; i++) {
            int pos = 0;
            while (numList.get(pos) != queries[i]) {   // Find position of queries[i] in numList
                pos++;
            }
            ans.add(pos);
            while (pos > 0) {   // Bring number at pos to the front
                int tmp = numList.get(pos);
                numList.set(pos, numList.get(pos-1));
                numList.set(pos-1, tmp);
                pos -= 1;
            }
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
}