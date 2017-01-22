from challenges import running_median
from expects import *

with description('RunningMedianList'):
    with before.each:
        self.list = running_median.RunningMedianList()

    with description('#append'):
        with it('inserts the item into the list in sorted order'):
            self.list.append(2)
            self.list.append(3)
            self.list.append(1)
            expect(self.list.list).to(equal([1, 2, 3]))

    with description('#median'):
        with context('when the list length is odd'):
            with it('returns the value of the middle item as a float'):
                self.list.append(2)
                self.list.append(3)
                self.list.append(1)
                expect(self.list.median()).to(equal(2.0))
        with context('when the list length is even'):
            with it('returns the mean of the middle two items as a float'):
                self.list.append(2)
                self.list.append(3)
                self.list.append(1)
                self.list.append(7)
                expect(self.list.median()).to(equal(2.5))
