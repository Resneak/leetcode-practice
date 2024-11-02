class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min == None:
            self.min = f",{val}"
        else:
            if val <= int(self.min.split(',')[-1]):
                self.min += f",{val}"


    def pop(self) -> None:
        RemovedValue = self.stack.pop()

        if RemovedValue == int(self.min.split(',')[-1]):
            List = self.min.split(',')
            List.pop()
            self.min = ','.join(List)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return int(self.min.split(',')[-1])


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()