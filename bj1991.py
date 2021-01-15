class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

def preOrder(node):
    print(node.root, end='')
    if node.left != '.':
        preOrder(tree[node.left])
    if node.right != '.':
        preOrder(tree[node.right])

def inOrder(node):
    if node.left != '.':
        inOrder(tree[node.left])
    print(node.root, end='')
    if node.right != '.':
        inOrder(tree[node.right])

def postOrder(node):
    if node.left != '.':
        postOrder(tree[node.left])
    if node.right != '.':
        postOrder(tree[node.right])
    print(node.root, end='')


N = int(input())

#트리구조 생성
tree = {}
for i in range(N):
    root, left, right = input().split()
    tree[root] = Node(root, left, right)

#전위순회(루트->왼쪽자식->오른쪽자식)
preOrder(tree['A'])
print()
#중위순회(왼쪽자식->루트->오른쪽자식)
inOrder(tree['A'])
print()
#후외순회(왼쪽자식->오른쪽자식->루트)
postOrder(tree['A'])
