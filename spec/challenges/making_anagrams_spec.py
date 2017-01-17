from challenges import making_anagrams
from expects import *

with description('number_needed'):
    with context('when a and b are totally disjointed'):
        with it('is the sum of the two string lengths'):
            a = 'zyabc'
            b = 'def'
            expect(making_anagrams.number_needed(a, b)).to(equal(len(a) + len(b)))
    with context("when a is 'abc' and b is 'cde'"):
        with it('is 4'):
            expect(making_anagrams.number_needed('abc', 'cde')).to(equal(4))
    with context ('when the two strings are identical'):
        with it('is 0'):
            a = 'abc'
            b = a[:]
            expect(making_anagrams.number_needed(a, b)).to(equal(0))
    with context('when the two strings have the same number of each character'):
        with it('is 0'):
            a = 'bbccdd'
            b = 'bcdbcd'
            expect(making_anagrams.number_needed(a, b)).to(equal(0))