# Q.1 implement Binary tree
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
def insert(root,data):
    if root is None:
        return Node(data)
    else:
        if root.data < data:
            root.right = insert(root.right,data)
        else:
            root.left = insert(root.left,data)
    return root
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)
root = None
root = insert(root,50)
insert(root,30)
insert(root,20)
insert(root,40)
insert(root,70)
insert(root,60)
insert(root,80)
inorder_traversal(root)

        

