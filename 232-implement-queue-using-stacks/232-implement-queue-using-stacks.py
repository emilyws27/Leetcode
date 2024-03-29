class MyQueue:

    def __init__(self):
        self.st = []

    def push(self, x):
        if len(self.st) == 0:
            self.st.append(x)
            return
        tmp = self.st.pop(-1)
        self.push(x)
        self.st.append(tmp)

    def pop(self):
        return self.st.pop(-1)

    def peek(self):
        return self.st[-1]

    def empty(self):
        return len(self.st) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()