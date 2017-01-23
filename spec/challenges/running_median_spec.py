from challenges import running_median
from expects import *

with description('RunningMedianList'):
    with before.each:
        self.list = running_median.RunningMedianList()

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
        with context('when testing supplied examples'):
            with context('when the list is [12]'):
                with it('returns 12.0'):
                    self.list.append(12)
                    expect(self.list.median()).to(equal(12.0))
            with context('when the list is [12, 4]'):
                with it('returns 8.0'):
                    self.list.append(12)
                    self.list.append(4)
                    expect(self.list.median()).to(equal(8.0))
            with context('when the list is [12, 4, 5]'):
                with it('returns 5.0'):
                    self.list.append(12)
                    self.list.append(4)
                    self.list.append(5)
                    expect(self.list.median()).to(equal(5.0))
            with context('when the list is [12, 4, 5, 3]'):
                with it('returns 4.5'):
                    self.list.append(12)
                    self.list.append(4)
                    self.list.append(5)
                    self.list.append(3)
                    expect(self.list.median()).to(equal(4.5))
            with context('when the list is [12, 4, 5, 3, 8]'):
                with it('returns 5.0'):
                    self.list.append(12)
                    self.list.append(4)
                    self.list.append(5)
                    self.list.append(3)
                    self.list.append(8)
                    expect(self.list.median()).to(equal(5.0))
            with context('when the list is [12, 4, 5, 3, 8, 7]'):
                with it('returns 6.0'):
                    self.list.append(12)
                    self.list.append(4)
                    self.list.append(5)
                    self.list.append(3)
                    self.list.append(8)
                    self.list.append(7)
                    expect(self.list.median()).to(equal(6.0))