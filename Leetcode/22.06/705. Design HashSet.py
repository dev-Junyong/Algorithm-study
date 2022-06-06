class MyHashSet:

    def __init__(self):
        self.chk_set = [-1] * 1000001

    def add(self, key: int) -> None:
        self.chk_set[key] = key


    def remove(self, key: int) -> None:
        self.chk_set[key] = -1


    def contains(self, key: int) -> bool:
        return self.chk_set[key] != -1



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)