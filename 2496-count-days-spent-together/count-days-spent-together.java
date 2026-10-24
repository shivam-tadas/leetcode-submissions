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

        System.out.println(aliceStart + " " + aliceEnd + " " + bobStart + " " + bobEnd);
        if (bobStart > aliceEnd || aliceStart > bobEnd)
            return 0;

        if (aliceStart < bobStart && aliceEnd > bobEnd)
            return bobEnd - bobStart + 1;

        if (bobStart < aliceStart && bobEnd > aliceEnd)
            return aliceEnd - aliceStart + 1;
            
        return Math.min(aliceEnd, bobEnd) - Math.max(aliceStart, bobStart) + 1;
    }
}