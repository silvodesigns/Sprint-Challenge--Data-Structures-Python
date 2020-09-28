class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.curr = 0

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.curr] = item
            self.curr = (self.curr + 1) % self.capacity
        else:
            self.data.append(item)
       

    def get(self):
        return self.data
    
    
    
    