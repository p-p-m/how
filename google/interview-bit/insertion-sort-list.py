# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def pprint(node):
    s = []
    n = node
    while n:
        s.append(str(n))
        n = n.next
    return ' > '.join(s)


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        return self.sort(A)

    def sort(self, A):
        root = A
        self.revert(A)
        i = root
        index = 0
        while i:
            j = i
            move = False
            while j.previous and j.val < j.previous.val:
                j = self.swap(j.previous, j)
                i = i.next
                move = True
            if not move:
                i = i.next
        while root.previous:
            root = root.previous
        return root

    def swap(self, a, b):
        a.next = b.next
        b.next = a
        b.previous = a.previous
        a.previous = b
        return b

    def revert(self, A):
        current = A
        current.previous = None
        while current.next:
            current.next.previous = current
            current = current.next


# A = [5, 66, 68, 42, 73, 25, 84, 63, 72, 20, 77, 38, 8, 99, 92, 49, 74, 45, 30, 51, 50, 95, 56, 19, 31, 26, 98, 67, 100, 2, 24, 6, 37, 69, 11, 16, 61, 23, 78, 27, 64, 87, 3, 85, 55, 22, 33, 62]
A = [2, 3, 1, 5, 4]
root = current = ListNode(A[0])
for el in A[1:]:
    node = ListNode(el)
    current.next = node
    current = node

s = Solution()
print pprint(s.insertionSortList(root))
