from insert_sort_list import ListNode, Solution


def convert_list_to_linked_list(items):
    head = ListNode(items.pop(0))
    p = head
    for i in items:
        node = ListNode(i)
        p.next = node
        p = node
    return head


def convert_linked_list_to_list(head):
    p = head
    result = []
    while p:
        result.append(p.val)
        p = p.next
    return result


def test_sample1():
    input_ = [4, 2, 1, 3]
    expected = sorted(input_)
    head = convert_list_to_linked_list(input_)

    assert expected == convert_linked_list_to_list(
        Solution().insert_sort_list(head))


def test_sample2():
    input_ = [-1, 5, 3, 4, 0]
    expected = sorted(input_)
    head = convert_list_to_linked_list(input_)

    assert expected == convert_linked_list_to_list(
        Solution().insert_sort_list(head))
