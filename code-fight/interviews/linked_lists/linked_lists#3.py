# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def addTwoHugeNumbers(a, b):

    def revert(_ll):
        previous = None
        current = _ll
        while current:
            _next = current.next
            current.next = previous
            previous = current
            current = _next
        return previous

    a, b = revert(a), revert(b)
    additional = 0
    first = result = ListNode(0)
    while True:
        s = additional
        if a:
            s += a.value
            a = a.next
        if b:
            s += b.value
            b = b.next
        additional = int(s / 10000)
        result.value = s % 10000
        if a or b:
            result.next = ListNode(0)
            result = result.next
        else:
            break
    if additional:
        result.next = ListNode(additional)

    return revert(first)


def list_to_linked_list(l):
    _next = None
    for el in l[::-1]:
        node = ListNode(el)
        node.next = _next
        _next = node
    return node


ll1 = list_to_linked_list([1, 2, 3, 9999])
ll2 = list_to_linked_list([1, 2, 3, 2, 8888])
r = addTwoHugeNumbers(ll1, ll2)

while r:
    print(r.value)
    r = r.next
