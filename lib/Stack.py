class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) <= self.limit:
            self.items.append(item)
        else:
            raise Exception()

    def pop(self):
        if len(self.items) != 0:
            self.items.pop()
            return 1

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        return -1