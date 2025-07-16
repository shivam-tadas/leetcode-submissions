class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"
        stk = []
        tmp = 0

        for i in tokens:
            if i in ops:
                n1, n2 = stk.pop(), stk.pop()
                if i == "+":
                    tmp = n2 + n1
                elif i == "-":
                    tmp = n2 - n1
                elif i == "*":
                    tmp = n2 * n1
                else:
                    tmp = int(n2 / n1)
                stk.append(tmp)
            else:
                stk.append(int(i))

        return stk.pop()