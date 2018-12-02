# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def isListPalindrome(ll):

    def revert(_ll):
        previous = None
        current = _ll
        while current:
            _next = current.next
            current.next = previous
            previous = current
            current = _next
        return previous

    def get_length(_ll):
        n = 0
        current = _ll
        while current:
            current = current.next
            n += 1
        return n

    first = current = ll
    middle = int((get_length(ll) + 1) / 2)
    i = 0
    while i != middle:
        i += 1
        current = current.next

    second = revert(current)
    while second:
        if second.value != first.value:
            return False
        first = first.next
        second = second.next
    return True


def list_to_linked_list(l):
    _next = None
    for el in l[::-1]:
        node = ListNode(el)
        node.next = _next
        _next = node
    return node


ll = list_to_linked_list([1, 2, 3, 2, 1])
print(isListPalindrome(ll))

# while ll:
#     print(ll.value)
#     ll = ll.next
