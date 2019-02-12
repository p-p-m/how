# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        node = self
        s = []
        while node:
            s.append(str(node.val))
            node = node.next
        return ' > '.join(s)

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        print A
        return self.sort(A)

    def sort(self, pivot, right_limit=None, left_origin=None):
        root = left = right = pivot
        current = right.next
        while current and current is not right_limit:
            if current.val < pivot.val:
                next = current.next
                current.next = left
                left = current
                right.next = next
                current = right.next
            else:
                right = current
                current = right.next
        print 'left', left
        print 'right', right
        print 'root', root
        if left_origin:
            left_origin.next = left
        if right_limit:
            right.next = right_limit
        if left is not root:
            print '\nsorting left with right limit', root
            left = self.sort(left, right_limit=root)
        if right is not root:
            print '\nsorting right with left limit', root
            self.sort(root.next, left_origin=root)
        return left


A = [5, 66, 68, 42, 73, 8, 99, 49]
# A = [9, 9, 7, 2, 3, 1, 5, 4, 2, 2, 2]
root = current = ListNode(A[0])
for el in A[1:]:
    node = ListNode(el)
    current.next = node
    current = node

s = Solution()
print s.sortList(root)
