class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        Map<Integer, List<Integer>> mapping = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();

        for (int i = 0; i < groupSizes.length; i++) {
            if (mapping.containsKey(groupSizes[i]))
                mapping.get(groupSizes[i]).add(i);
            else
                mapping.put(groupSizes[i], new ArrayList<>(List.of(i)));
        }

        mapping.forEach((size, persons) -> {
            List<Integer> curr = new ArrayList<>();
            for (int i = 0; i < persons.size(); i++) {
                if (i != 0 && i % size == 0) {
                    ans.add(curr);
                    curr = new ArrayList<>();
                }
                curr.add(persons.get(i));
            }
            if (curr.size() > 0) ans.add(curr);
        });

        return ans;
    }
}