class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.next_oldest_value = 0
        self.items = [None for item in range(capacity)]

    def append(self, item):

        self.items[self.next_oldest_value] = item

        self.next_oldest_value += 1
        if self.next_oldest_value > (self.capacity - 1):
            self.next_oldest_value = 0

    def get(self):
        return [item for item in self.items if item is not None]
