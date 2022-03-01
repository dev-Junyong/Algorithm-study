class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.cur_range = []

    def next(self, val: int) -> float:
        if len(self.cur_range) == self.size:
            self.cur_range.pop(0)
        self.cur_range.append(val)
        return sum(self.cur_range) / len(self.cur_range)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)