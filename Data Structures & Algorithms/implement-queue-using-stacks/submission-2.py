class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def move(self):
        if self.stack_out: return 
        while self.stack_in:
            el = self.stack_in.pop()
            self.stack_out.append(el)

    def pop(self) -> int:
        self.move()
        pop = self.stack_out.pop()
        return pop

    def peek(self) -> int:
        self.move()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()