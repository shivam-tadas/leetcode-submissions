class MyQueue:

    def __init__(self):
        self.inS = []
        self.outS = []

    def push(self, x: int) -> None:
        self.inS.append(x)

    def pop(self) -> int:
        self.peek() # Transfer from in to out, reversing it
        return self.outS.pop()

    def peek(self) -> int:
        if not self.outS:
            while self.inS:  # Transfer content from in to out, reversing it
                self.outS.append(self.inS.pop())

        return self.outS[-1]

    def empty(self) -> bool:    # No element present
        return not self.inS and not self.outS


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()