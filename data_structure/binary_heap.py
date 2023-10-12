class Binaryheap(object):
    def __init__(self):
        self.items = [None]
    
    def __len__(self):
        return len(self.items) - 1
    
    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]

            i = parent
            parent // 2
    

