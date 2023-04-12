import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

inorder_list = list(map(int, sys.stdin.readline().split()))
postorder_list = list(map(int, sys.stdin.readline().split()))

index_list = [0 for _ in range(n+1)]

for i in range(n):
    index_list[inorder_list[i]] = i

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return None

    present_node = postorder_list[post_end]

    inorder_index = index_list[present_node]

    left_node = inorder_index - in_start
    right_node = in_end - inorder_index

    print(present_node, end=" ")
    preorder(in_start, inorder_index-1, post_start, post_start+left_node-1)
    preorder(inorder_index+1, in_end, post_end-right_node, post_end-1)

preorder(0, n-1, 0, n-1)
