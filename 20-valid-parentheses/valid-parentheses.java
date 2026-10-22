class Solution {
    public boolean isValid(String s) {
        Deque<Character> stk = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i);
            if (curr == '(' || curr == '[' || curr == '{')
                stk.push(curr);
            else if (!stk.isEmpty()) {
                if (curr == ')' && stk.peek() == '(') stk.pop();
                else if (curr == ']' && stk.peek() == '[') stk.pop();
                else if (curr == '}' && stk.peek() == '{') stk.pop();
                else return false;
            }
            else return false;
        }
        

        return stk.isEmpty();
    }
}