import heapq
class RunningMedianList:
    def __init__(self):
        # Store the current median here
        self.med = None
        self.left = []
        self.right = []
        # diff > 0 means the structure is heavy to the right
        # diff < 0 means the structure is heavy to the left
        self.diff = 0

    def append(self, item):
        if not self.med:
            self.med = item
        elif item > self.med:
            heapq.heappush(self.right, item)
            self.diff += 1
        else:
            heapq.heappush(self.left, -item)
            self.diff -= 1

        self.balance()

    def balance(self):
        if self.diff > 1:
            # We are right heavy
            heapq.heappush(self.left, -self.med)
            self.med = heapq.heappop(self.right)
            self.diff -= 2
            return self.balance()
        elif self.diff < -1:
            # We are left heavy
            heapq.heappush(self.right, self.med)
            self.med = (-heapq.heappop(self.left))
            self.diff += 2
            return self.balance()
        else:
            return

    def count_of_items(self):
        if not self.med:
            return 0
        else:
            return 1 + len(self.left) + len(self.right)

    def median(self):
        i = self.count_of_items()
        if i == 0:
            raise ValueError('Empty heap')
        elif i % 2 == 1:
            return self.med / 1
        elif i % 2 == 0:
            # When i is 2 one side has one node, the other side is empty
            if self.diff == 1:
                return (self.med + self.right[0]) / 2
            else:
                return (self.med - self.left[0]) / 2



