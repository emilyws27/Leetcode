class RandomizedSet:

    def __init__(self):
        self.items = set()
        
    def insert(self, val):
        if val not in self.items:
            self.items.add(val)
            return True
        return False
        
    def remove(self, val):
        if val in self.items:
            self.items.remove(val)
            return True
        return False
        
    def getRandom(self):
        return random.sample(self.items, 1).pop()

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()