class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        List<Integer> monthDays = new ArrayList<>(), cummulativeMonthDays = new ArrayList<>();
        monthDays.add(31);
        monthDays.add(28);
        monthDays.add(31);
        monthDays.add(30);
        monthDays.add(31);
        monthDays.add(30);
        monthDays.add(31);
        monthDays.add(31);
        monthDays.add(30);
        monthDays.add(31);
        monthDays.add(30);
        monthDays.add(31);
        int cummulative = 0;
        cummulativeMonthDays.add(0);
        for (int i: monthDays) {
            cummulative += i;
            cummulativeMonthDays.add(cummulative);
        }
        Integer aliceStart, aliceEnd, bobStart, bobEnd;
        aliceStart = new Integer(cummulativeMonthDays.get(new Integer(arriveAlice.substring(0,2))-1) + new Integer(arriveAlice.substring(3,5)));
        aliceEnd = new Integer(cummulativeMonthDays.get(new Integer(leaveAlice.substring(0,2))-1) + new Integer(leaveAlice.substring(3,5)));
        bobStart = new Integer(cummulativeMonthDays.get(new Integer(arriveBob.substring(0,2))-1) + new Integer(arriveBob.substring(3,5)));
        bobEnd = new Integer(cummulativeMonthDays.get(new Integer(leaveBob.substring(0,2))-1) + new Integer(leaveBob.substring(3,5)));

        int ans = 0;
        for (int i = Math.min(Math.min(aliceStart, aliceEnd), Math.min(bobStart, bobEnd)); i <= Math.max(Math.max(aliceStart, aliceEnd), Math.max(bobStart, bobEnd)); i++)
            if (i >= aliceStart && i <= aliceEnd && i >= bobStart && i <= bobEnd)
                ++ans;

        return ans;
    }
}