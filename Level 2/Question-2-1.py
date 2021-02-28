"""
Google Solution #2

Build a function that takes in H, Z and returns X
H = Height of the Binary Search Tree (BST)
Z = Values to find the position in the BST
X = Values above the positions identified from Z

Build a Perfect BST using only the height as H. Take the values from Z
return the node above it in a list.

"""


def max_node(tree_height):
    max_value = (2 ** tree_height - 1)
    return max_value


def find_parent_node(max_value, index):
    if max_value < index:
        parent = -1
    else:
        parent = process_bst(max_value, index)
    return parent


def process_bst(max_value, index):
    node_value = 0
    the_result = -1
    sub_tree = max_value
    flag = True
    while flag:
        if sub_tree == 0:
            flag = False
        sub_tree = sub_tree >> 1
        left = node_value + sub_tree
        right = left + sub_tree
        the_node = right + 1
        if left == index:
            the_result = the_node
            flag = False
        elif right == index:
            the_result = the_node
            flag = False
        elif index > left:
            node_value = left
    return the_result


def solution(tree_height, child_node):
    max_value = max_node(tree_height)
    results = [find_parent_node(max_value, index) for index in child_node]
    return results


if __name__ == '__main__':
    h = 5
    z = [19, 14, 28]
    rl = solution(h, z)
