# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if not A or not A.next:
            return A

        root = previous = None
        current = A
        while current:
            if self.can_go(current):
                current = self.go(current)
            else:
                if root is None:
                    root = previous = current
                else:
                    previous.next = current
                    previous = current
                current = current.next
        if previous:
            previous.next = None

        return root

    def can_go(self, node):
        return node.next and node.next.val == node.val

    def go(self, node):
        current = node
        while current.next and current.val == current.next.val:
            current = current.next
        return current.next



class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if not A: return None
        slow = fast = A
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break

        if slow != fast: return None
        slow = A
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

