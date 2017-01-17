from challenges import ransom_note
from expects import *

with description('ransom_note'):
    with context('when the magazine contains all the required words for the note'):
        with it('is true'):
            expect(ransom_note.ransom_note(['foo', 'Bar', 'baz'], ['baz', 'Bar'])).to(be_true)
    with context('when the magazine does not contain all of the required words for the note'):
        with it('is false'):
            expect(ransom_note.ransom_note(['foo', 'bar', 'baz'], ['baz', 'Bar'])).to(be_false)