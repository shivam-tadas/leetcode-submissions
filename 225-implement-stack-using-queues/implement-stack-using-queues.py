class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        if self.q1:
            return self.q1.popleft()

        while len(self.q2) > 0:
            self.q1.append(self.q2.popleft())
        
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        return self.q1.popleft()

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        if self.q1:
            n = self.q1.popleft()
            self.q2.append(n)
            return n

        while len(self.q2) > 1:
            self.q1.append(self.q2.popleft())

        n = self.q2.popleft()
        self.q1.append(n)
        return n

    def empty(self) -> bool:
        return not self.q1 and not self.q2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()