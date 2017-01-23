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

    with description('#set_child'):
        with context('when a child with the value is already in children'):
            with it('raises a ValueError'):
                def callback():
                    child2 = prefix_tree.PrefixTreeNode('d')
                    self.node.set_child(child2)

                child = prefix_tree.PrefixTreeNode('d')
                self.node.set_child(child)
                expect(callback).to(raise_error(ValueError))
        with context('when a child with the value is not in children'):
            with it('adds the child to children'):
                expect(self.node.find_child('d')).to(be_none)

                child = prefix_tree.PrefixTreeNode('d')
                self.node.set_child(child)

                expect(self.node.find_child('d')).to(be(child))

    with description('#total_children'):
        with context('when the children are all leaf nodes'):
            with it('is the count of children'):
                child0 = prefix_tree.PrefixTreeNode('d')
                child1 = prefix_tree.PrefixTreeNode('f')
                child2 = prefix_tree.PrefixTreeNode('g')
                self.node.set_child(child0)
                self.node.set_child(child1)
                self.node.set_child(child2)

                expect(self.node.total_children()).to(be(3))
        with context('when there are leaf nodes in children and in children of children'):
            with it('is the count of all children'):
                child0 = prefix_tree.PrefixTreeNode('d')
                child1 = prefix_tree.PrefixTreeNode('f')
                child2 = prefix_tree.PrefixTreeNode('g')
                self.node.set_child(child0)
                child1.set_child(child2)
                self.node.set_child(child1)

                expect(self.node.total_children()).to(be(3))



