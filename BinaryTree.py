print("________ Tree in Python _______")

from binarytree import Node
root=Node(3)
root.left=Node(5)
root.right=Node(9)
root.root=Node(4)
print("Binary Tree:",root)
print("List:",list(root))
print("Inorder of nodes:",root.inorder)
print("Size of Tree:",root.size)
print("Height of Tree:",root.height)

print("_________________________________________________")

from binarytree import build
nodes={1,2,3,4,5,6,7,8,99}
Binary=build(nodes)
print("Binary Tree:",Binary)
print("List:",list(Binary))
print("Inorder of nodes:",Binary.inorder)
print("Size of Tree:",Binary.size)
print("Height of Tree:",Binary.height)
