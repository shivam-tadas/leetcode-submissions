class Solution {
    Set<Integer> validStates;

    public List<String> readBinaryWatch(int turnedOn) {
        validStates = new HashSet<>();

        readBinaryWatchHelper(turnedOn, 0, 0);

        int h, m;
        String curr;
        List<String> ans = new ArrayList<>();
        for (int i: validStates) {
            h = i / 60;
            m = i % 60;
            if (m < 10)
                curr = h + ":0" + m;
            else
                curr = h + ":" + m;
            ans.add(curr);
        }

        return ans;
    }

    private void readBinaryWatchHelper(int remaining, int hour, int min) {
        if (hour > 11 || min > 59) return;

        if (remaining == 0) {
            validStates.add(hour*60 + min);
            return;
        }

        for (int i = 1; i <= 8; i *= 2) {
            if ((hour | i) == hour || (hour | i) > 11) continue;
            readBinaryWatchHelper(remaining-1, hour | i, min);
        }
        for (int i = 1; i <= 32; i *= 2) {
            if ((min | i) == min || (min | i) > 59) continue;
            readBinaryWatchHelper(remaining-1, hour, min | i);
        }
    }
}