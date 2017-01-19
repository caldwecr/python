from challenges import is_bst
from expects import *

class FauxBTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

with description('check_binary_search_tree_'):
    with context('when node is a leaf node'):
        with it('is true'):
            node = FauxBTNode(1)
            expect(is_bst.check_binary_search_tree_(node)).to(be_true)
    with context('when node is not a leaf node'):

        with before.each:
            self.node = FauxBTNode(100)

        with context('when a descendant of left > root'):
            with it('is false'):
                self.node.left = FauxBTNode(75)
                self.node.left.right = FauxBTNode(125)
                expect(is_bst.check_binary_search_tree_(self.node.left)).to(be_true)
                expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)

        with context('when left is None'):
            with context('when right is not None'):
                with context('when right is not a BST'):
                    with it('is false'):
                        self.node.right = FauxBTNode(200)
                        self.node.right.right = FauxBTNode(150)
                        expect(is_bst.check_binary_search_tree_(self.node.right)).to(be_false)
                        expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)
                with context('when right is a BST'):
                    with context('when right < data'):
                        with it('is false'):
                            self.node.right = FauxBTNode(70)
                            expect(is_bst.check_binary_search_tree_(self.node.right)).to(be_true)
                            expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)
                    with context('when right == data'):
                        with it('is false'):
                            self.node.right = FauxBTNode(100)
                            expect(is_bst.check_binary_search_tree_(self.node.right)).to(be_true)
                            expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)
                    with context('when right > data'):
                        with it('is true'):
                            self.node.right = FauxBTNode(200)
                            expect(is_bst.check_binary_search_tree_(self.node.right)).to(be_true)
                            expect(is_bst.check_binary_search_tree_(self.node)).to(be_true)

        with context('when left is not None'):
            with context('when right is None'):

                with context('when left is a BST'):
                    with context('when data > left.data'):
                        with it('is true'):
                            self.node.left = FauxBTNode(50)
                            expect(is_bst.check_binary_search_tree_(self.node)).to(be_true)
                    with context('when data <= left.data'):
                        with it('is false'):
                            self.node.left = FauxBTNode(105)
                            expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)
                with context('when left is not a BST'):
                    with it('is false'):
                        self.node.left = FauxBTNode(50)
                        self.node.left.left = FauxBTNode(55)
                        expect(is_bst.check_binary_search_tree_(self.node.left)).to(be_false)
                        expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)

            with context('when right is not None'):
                with context('when left is not a BST'):
                    with it('is false'):
                        self.node.right = FauxBTNode(200)
                        self.node.left = FauxBTNode(50)
                        self.node.left.left = FauxBTNode(55)
                        expect(is_bst.check_binary_search_tree_(self.node.right)).to(be_true)
                        expect(is_bst.check_binary_search_tree_(self.node.left)).to(be_false)
                        expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)
                with context('when right is not a BST'):
                    with it('is false'):
                        self.node.right = FauxBTNode(200)
                        self.node.left = FauxBTNode(50)
                        self.node.right.right = FauxBTNode(150)
                        expect(is_bst.check_binary_search_tree_(self.node.right)).to(be_false)
                        expect(is_bst.check_binary_search_tree_(self.node.left)).to(be_true)
                        expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)
                with context('when both left and right are BST'):
                    with context('when left >= node'):
                        with it('is false'):
                            self.node.right = FauxBTNode(200)
                            self.node.left = FauxBTNode(120)
                            expect(is_bst.check_binary_search_tree_(self.node.right)).to(be_true)
                            expect(is_bst.check_binary_search_tree_(self.node.left)).to(be_true)
                            expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)
                            self.node.left = FauxBTNode(100)
                            expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)
                    with context('when right <= node'):
                        with it('is false'):
                            self.node.right = FauxBTNode(70)
                            self.node.left = FauxBTNode(50)
                            expect(is_bst.check_binary_search_tree_(self.node.right)).to(be_true)
                            expect(is_bst.check_binary_search_tree_(self.node.left)).to(be_true)
                            expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)
                            self.node.right = FauxBTNode(100)
                            expect(is_bst.check_binary_search_tree_(self.node)).to(be_false)

