# Definition for singly-linked list:
class ListNode(object):

    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(ll, k):
    first = None
    while first is None and ll:
        if ll.value != k:
            first = ll
        ll = ll.next

    current = first
    while current and current.next:
        if current.next.value == k:
            current.next = current.next.next
        else:
            current = current.next
    return first


def list_to_linked_list(l):
    _next = None
    for el in l[::-1]:
        node = ListNode(el)
        node.next = _next
        _next = node
    return node


ll = list_to_linked_list([1, 2, 3, 3, 3, 3, 5, 5])
ll = removeKFromList(ll, 3)

while ll:
    print(ll.value)
    ll = ll.next

