class RunningMedianList:
    def __init__(self, existing_list = []):
        self.list = sorted(existing_list)

    def append(self, item):
        self.list.append(item)
        self.list.sort()

    def median(self):
        if len(self.list) % 2 == 1:
            return self.list[len(self.list)//2]/1
        else:
            m = len(self.list)//2
            return (self.list[m] + self.list[m-1])/2


