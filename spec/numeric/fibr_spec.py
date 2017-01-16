from numeric import fibr
from expects import *

with description('fibr'):
    with description('fib'):
        with it('returns the fib seq'):
            expect(fibr.fib(4)).to(equal([1, 1, 2, 3]))
    with description('fib_rec'):
        with it('returns the fib seq'):
            expect(fibr.fib_rec(3)).to(equal([1, 1, 2]))



