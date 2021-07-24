class OrderedStream:

    def __init__(self, n: int):
        self.stream = [0] * n
        # self.stream = [0, 0, 0, 0, 0]
        self.pointer = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        # self.stream = [0, 0, "ccccc", 0, 0]
        result = []
        for item in self.stream[self.pointer:]:
            if item == 0:
                break
            self.pointer += 1
            result.append(item)
        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)