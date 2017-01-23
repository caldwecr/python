from challenges import prefix_tree
from expects import *

with description('PrefixTreeNode'):
    with before.each:
        self.node = prefix_tree.PrefixTreeNode('c')

    with description('instantiation'):
        with it('has the value passed as an argument'):
            expect(self.node.value).to(equal('c'))

    with description('#find_child'):
        with context('when a child node with the specified value does not exist'):
            with it('is None'):
                expect(self.node.find_child('d')).to(be_none)
        with context('when a child node with the specified value exists'):
            with it('returns the node'):
                child = prefix_tree.PrefixTreeNode('d')
                self.node.set_child(child)
                expect(self.node.find_child('d')).to(be(child))

    with description('#find_or_create_child'):
        with context('when a child node with the specified value does not exist'):
            with it('is a PrefixTreeNode with the specified value'):
                res = self.node.find_or_create_child('d')
                expect(res).to(be_a(prefix_tree.PrefixTreeNode))
                expect(res.value).to(equal('d'))
            with it('adds the child to the children'):
                expect(self.node.children.keys()).not_to(contain('d'))

                self.node.find_or_create_child('d')

                expect(self.node.children.keys()).to(contain('d'))
                child = self.node.children['d']
                expect(child).to(be_a(prefix_tree.PrefixTreeNode))
                expect(child.value).to(equal('d'))
        with context('when a child node with the specified value exists in children'):
            with it('returns the existing child'):
                child = prefix_tree.PrefixTreeNode('d')
                self.node.set_child(child)
                expect(self.node.find_or_create_child('d')).to(be(child))

