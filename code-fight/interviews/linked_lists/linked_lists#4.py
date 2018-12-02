class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def mergeTwoLinkedLists(ll1, ll2):
    def gen(ll1, ll2):
        while ll1 or ll2:
            if ll1 is not None and (ll2 is None or ll1.value < ll2.value):
                yield ll1
                ll1 = ll1.next
            else:
                yield ll2
                ll2 = ll2.next

    _gen = gen(ll1, ll2)
    try:
        first = current = next(_gen)
    except StopIteration:
        return None
    for el in _gen:
        current.next = el
        current = el

    return first


def list_to_linked_list(l):
    _next = None
    for el in l[::-1]:
        node = ListNode(el)
        node.next = _next
        _next = node
    return node


ll1 = list_to_linked_list([1, 2, 3, 9999])
ll2 = list_to_linked_list([1, 2, 3, 6, 8888])

r = mergeTwoLinkedLists(ll1, ll2)

while r:
    print(r.value)
    r = r.next

