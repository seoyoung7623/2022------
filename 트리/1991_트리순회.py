# 1991 트리순회 S1
import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for n in range(N):
    root,left,right = input().strip().split()
    tree[root] = [left, right]

def preOrder(root):
    if root != '.':
        print(root,end='')
        preOrder(tree[root][0])
        preOrder(tree[root][1])

def inOrder(root):
    if root != '.':
        inOrder(tree[root][0])
        print(root,end='')
        inOrder(tree[root][1])

def postOrder(root):
    if root != '.':
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root,end='')
        
preOrder('A')
print()
inOrder('A')
print()
postOrder('A')