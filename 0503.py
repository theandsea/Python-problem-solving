class Node:
    def __init__(self, val: int = 0, left=None, right=None):
        """
        initialize a node
        :param val:
        :param left:
        :param right:
        """
        assert isinstance(left, Node) or left is None
        assert isinstance(right, Node) or right is None
        self.val = val
        self.left = left
        self.right = right


def insert(root, num):
    """
    insert a value into a tree
    :param root:
    :param num:
    :return:
    """
    assert isinstance(root, Node) and isinstance(num, int)
    curr = root
    while curr is not None:
        if num < curr.val:
            if curr.left is not None:
                curr = curr.left
            else:
                curr.left = Node(num)
                return curr.val
        else:
            if curr.right is not None:
                curr = curr.right
            else:
                curr.right = Node(num)
                return curr.val


def get_tree_list(p):
    """
    takes a permutation p as input and returns a list that represents the binary tree
    :param p:
    :return:
    """
    assert isinstance(p, list)
    maxnum = 0
    dic = {}
    for num in p:
        assert isinstance(num, int) and num >= 0
        if num in dic.keys():
            assert False
        else:
            dic[num] = True
        maxnum = max(maxnum, num)

    res = [0 for i in range(maxnum + 1)]
    res[p[0]] = p[0]  # root

    root = Node(p[0])
    for i in range(1, len(p)):
        res[p[i]] = insert(root, p[i])

    return res


"""
p=[8, 5, 1, 10, 0, 4, 2, 3, 7, 9, 6]
print(get_tree_list(p))
"""
