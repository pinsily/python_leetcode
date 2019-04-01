import sys
sys.path.append("../")

from leetcode_utils import run_function

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_link(nums: list) -> ListNode:
    head = rt = ListNode(0)
    for ele in nums:
        new_node = ListNode(ele)
        rt.next = new_node
        rt = rt.next

    return head.next


def add_two_numbers_1(l1: ListNode, l2: ListNode) -> ListNode:
    """[summary]

    [description]
    :param
        l1: [ListNode]
        l2: [ListNode]

    :returns: [ListNode]
    """
    head = rt = ListNode(0)
    count = 0
    while l1 != None and l2 != None:
        temp_sum = l1.val + l2.val + count
        sums, count = (temp_sum % 10, 1) if temp_sum >= 10 else (temp_sum, 0)
        new_node = ListNode(sums)
        rt.next = new_node
        rt = rt.next
        l1 = l1.next
        l2 = l2.next

    while l1 != None:
        sums, count = ((l1.val + count) % 10, 1) if (l1.val +
                                                     count) >= 10 else (l1.val + count, 0)
        new_node = ListNode(sums)
        rt.next = new_node
        rt = rt.next
        l1 = l1.next

    while l2 != None:
        sums, count = ((l2.val + count) % 10, 1) if (l2.val +
                                                     count) >= 10 else (l2.val + count, 0)
        new_node = ListNode(sums)
        rt.next = new_node
        rt = rt.next
        l2 = l2.next

    if count > 0:
        new_node = ListNode(count)
        rt.next = new_node

    return head.next


def add_two_numbers_2(l1: ListNode, l2: ListNode) -> ListNode:
    """[summary]

    [这种方法是真的妙很多，而且效率快了一半]
    :param
        l1: [ListNode]
        l2: [ListNode]

    :returns: [ListNode]
    """
    r = tmp = ListNode(0)
    rest = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        s = x + y + rest
        r.next = ListNode(s % 10)
        rest = s / 10
        r = r.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if rest > 0:
        r.next = ListNode(1)
    return tmp.next


link_1 = create_link([2, 4, 3])
link_2 = create_link([5, 6, 4])
run_function(1, add_two_numbers_1, link_1, link_2)
run_function(2, add_two_numbers_2, link_1, link_2)
