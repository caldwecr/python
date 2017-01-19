from challenges import balanced_brackets
from expects import *

with description('is_matched'):
    with context('when the string is a simple pair'):
        with it('is true'):
            expect(balanced_brackets.is_matched('{}')).to(be_true)
    with context('when the string is an unmatched pair'):
        with it('is false'):
            expect(balanced_brackets.is_matched('{]')).to(be_false)
    with context('when the string is just one lefty'):
        with it('is false'):
            expect(balanced_brackets.is_matched('{')).to(be_false)
    with context('when the string is just one righty'):
        with it('is false'):
            expect(balanced_brackets.is_matched(')')).to(be_false)
    with context('when brackets are nested, balanced, and symmetric'):
        with it('is true'):
            expect(balanced_brackets.is_matched('{([])}')).to(be_true)
    with context('when there quantity of brackets is balanced but the ordering is unbalanced'):
        with it('is false'):
            expect(balanced_brackets.is_matched('{([)]}')).to(be_false)
    with context('when a balanced bracket is the same type as the enclosing balanced bracket'):
        with it('is true'):
            expect(balanced_brackets.is_matched('{[{()}]}')).to(be_true)
    with context('when balanced brackets occur consecutively unnested'):
        with it('is true'):
            expect(balanced_brackets.is_matched('{[(){}][]()}')).to(be_true)