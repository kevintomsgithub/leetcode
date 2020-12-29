# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def get_number(self, node):
        number = []
        while node != None:
            number.insert(0, node.val)
            node = node.next
        return int(''.join(map(str, number)))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.get_number(l1)
        b = self.get_number(l2)
        c = a + b
        # d = list(map(int, reversed(list(str(c)))))
        d = list(map(int, list(str(c))))
        prev = None
        root = None
        for index, i in enumerate(d):
            x = ListNode()
            if index+1 == len(d):
                root = x
            x.val = i
            x.next = prev
            prev = x
        return root