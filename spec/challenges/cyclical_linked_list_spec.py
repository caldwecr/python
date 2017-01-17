from challenges import cyclical_linked_list
from expects import *


class FauxNode(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

with description('has_cycle'):
    with before.each:
        self.node3 = FauxNode()
        self.node2 = FauxNode(next_node=self.node3)
        self.node1 = FauxNode(next_node=self.node2)
        self.node0 = FauxNode(next_node=self.node1)

    with context('when the list is cyclical'):
        with it('is True'):
            self.node3.next = self.node0
            expect(cyclical_linked_list.has_cycle(self.node0)).to(be_true)
    with context('when the list is not cyclical'):
        with it('is False'):
            expect(cyclical_linked_list.has_cycle(self.node0)).to(be_false)
    with context('when the list contains one node'):
        with context('when the node is the end of the list'):
            with it('is False'):
                expect(cyclical_linked_list.has_cycle(self.node3)).to(be_false)
        with context('when the node is linked to itself'):
            with it('is True'):
                self.node3.next = self.node3
                expect(cyclical_linked_list.has_cycle(self.node3)).to(be_true)
    with context('when the list is empty'):
        with it('is False'):
            expect(cyclical_linked_list.has_cycle(None)).to(be_false)