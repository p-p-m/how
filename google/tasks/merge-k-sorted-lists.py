# https://www.lintcode.com/problem/merge-k-sorted-lists/description

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        head = tail = None
        print('TEST')
        while any(lists):

            min_index, min_value = min(
                enumerate([l.val for l in lists if l.val is not None]),
                key=lambda el: el[1]
            )
            print('min_value', min_value)

            lists[min_index] = lists[min_index].next
            if tail is None:
                head = tail = ListNode(min_value)
            else:
                tail.next = ListNode(min_value)
                tail = tail.next
        while head:
            print(head.val)
            head = head.next
        return head

s = Solution()
s.mergeKLists([ListNode(1)])