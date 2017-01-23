import heapq
class RunningMedianList:
    def __init__(self):
        self.list = []

    def append(self, item):
        heapq.heappush(self.list, item)


    def median(self):
        n = len(self.list)//2 + 1
        nl = heapq.nlargest(n, self.list)

        if len(self.list) % 2 == 1:
            return nl[-1] / 1
        else:
            return (nl[-1] + nl[-2])/2


