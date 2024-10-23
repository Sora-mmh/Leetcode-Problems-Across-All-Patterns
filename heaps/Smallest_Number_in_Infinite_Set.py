class SmallestInfiniteSet:

    def __init__(self):
        self.counter = 1
        self.heap = set()


    def popSmallest(self) -> int:
        if self.heap:
            res = min(self.heap)
            self.heap.remove(res)
            return res
        else:
            res = self.counter
            self.counter += 1
            return res
        

    def addBack(self, num: int) -> None:
        if num < self.counter:
            self.heap.add(num)
            
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
