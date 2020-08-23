# Create Node Class
class N(object):
    def __init__(self, value):
        self.value = value
        self.Left = None
        self.Right = None

class BinaryTree(object):
    # first, initialize the root
    def __init__(self,root):
        self.root = N(root)

    # print traversal node
    def ReturnTree(self, traversal_type):
        if(traversal_type == "preorder"):
            return self.Preorder(tree.root, "")
        elif(traversal_type == "inorder"):
            return self.Inorder(tree.root, "")
        elif(traversal_type == "postorder"):
            return self.Postorder(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) +" is not supported.")
            return False

    # create function for preorder traversal
    """ ROOT --> LEFT --> RIGHT """
    def Preorder(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.Preorder(start.Left, traversal)
            traversal = self.Preorder(start.Right, traversal)
        return traversal

    # create function for Inorder traversal
    """ LEFT --> ROOT --> RIGHT """
    def Inorder(self, start, traversal):
        if start:
            traversal = self.Inorder(start.Left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.Inorder(start.Right, traversal)
        return traversal

    # create function for Postorder traversal
    """ LEFT --> RIGHT --> ROOT """
    def Postorder(self, start, traversal):
        if start:
            traversal = self.Postorder(start.Left, traversal)
            traversal = self.Postorder(start.Right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    #        1 
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7

    # preorder: 1 2 4 5 3 6 7
    # inorder : 4 2 5 1 6 3 7
    # postorder: 4 5 2 6 7 3 1

# setup tree
tree = BinaryTree(1)
tree.root.Left = N(2)
tree.root.Right = N(3)
tree.root.Left.Left = N(4)
tree.root.Left.Right = N(5)
tree.root.Right.Left = N(6)
tree.root.Right.Right = N(7)

type = input("Enter the traversal type: ")
print(tree.ReturnTree(type))