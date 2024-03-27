# Input = preorder:[3,9,20,15,7]  inorder:[9,3,15,20,7]
# Output= [3,9,20,null,null,15,7]

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def Constructbinarytreefrompreorderandinorder(preorder, inorder):
    if not preorder and not inorder:
        return None
    root = Node(preorder[0])
    mid = inorder.index(root.data)
    root.left = Constructbinarytreefrompreorderandinorder(
        preorder[1:mid+1], inorder[0:mid])
    root.right = Constructbinarytreefrompreorderandinorder(
        preorder[mid+1:], inorder[mid+1:])
    return root


def Constructbinarytreefrominorderandpostorder(inorder, postorder):
    if not postorder and not inorder:
        return None
    root = Node()
    root.data = postorder[-1]
    mid = inorder.index(root.data)
    root.left = Constructbinarytreefrominorderandpostorder(
        inorder[:mid], postorder[:mid])
    root.right = Constructbinarytreefrominorderandpostorder(
        inorder[mid+1:], postorder[mid+1:])
    return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(Constructbinarytreefrompreorderandinorder(preorder, inorder).data)
