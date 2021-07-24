class OrderedStream:
    _n = None
    values = None
    pointer = 1

    def __init__(self, n: int):
        if n < 1:
            raise Exception("n must be greater than 1")
        elif n > 1000:
            raise Exception("n must be lesser than 1000")
        self._n = n
        self.values = {}
    
    def validate_idKey(self, idKey: int):
        if idKey < 1:
            raise Exception("idKey must be greater than 1")
        elif idKey > self._n:
            raise Exception(f"idKey must be lesser than {self._n}")
    
    @staticmethod
    def validate_value(value: str):
        if len(value) != 5:
            raise Exception("value should have a length of 5")
        elif not value.islower():
            raise Exception("value should only consist of lowercase letters")
        
    def insert(self, idKey: int, value: str) -> List[str]:
        self.validate_idKey(idKey)
        self.validate_value(value)
        self.values.update({idKey: value})
        
        chunks = []
        for n in range(self.pointer-1, self._n):
            n += 1
            if n not in self.values.keys():
                self.pointer = n
                break

            if n == self.pointer:
                chunks.append(self.values[n])
                self.pointer += 1
        return chunks
                


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)