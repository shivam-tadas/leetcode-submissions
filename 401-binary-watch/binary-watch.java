class Solution {
    List<String> ans;

    public List<String> readBinaryWatch(int turnedOn) {
        ans = new ArrayList<>();

        int i, j;
        for (i = 0; i < 12; ++i)
            for (j = 0; j < 60; ++j)
                if (countSetBits(i, j) == turnedOn) {
                    if (j < 10) ans.add(i + ":0" + j);
                    else ans.add(i + ":" + j);
                } 

        return ans;
    }

    private static int countSetBits(int h, int m) {
        int ret = 0;
        while (h > 0) {
            ret += h & 1;
            h >>= 1;
        }

        while (m > 0) {
            ret += m & 1;
            m >>= 1;
        }

        return ret;
    }
}