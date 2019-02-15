class RandomListNode():
    def __init__(self, x: int):
        self.label = x
        self.next = None
        self.random = None


class Solution():
    def copy_random_list(self, root: RandomListNode) -> RandomListNode:
        head = None
        if root is not None:
            pointers = {}
            new_root = RandomListNode(root.label)
            pointers[id(root)] = new_root
            head = new_root
            while (root is not None and
                   (root.next is not None or root.random is not None)):
                if root.next is not None:
                    if id(root.next) not in pointers:
                        new_root.next = RandomListNode(root.next.label)
                        pointers[id(root.next)] = new_root.next
                    else:
                        new_root.next = pointers[id(root.next)]
                if root.random is not None:
                    if id(root.random) not in pointers:
                        new_root.random = RandomListNode(root.random.label)
                        pointers[id(root.random)] = new_root.random
                    else:
                        new_root.random = pointers[id(root.random)]
                root = root.next
                new_root = new_root.next
        return head
