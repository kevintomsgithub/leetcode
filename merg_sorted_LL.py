class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def sortLL(l1, l2):
    # Convert the data in LL to array/list
    l1_list = [1,2,4]
    l2_list = [1,3,4]
    sorted_list = []
    # while l1:
    # 	l1_list.append(l1.val)
    # 	l1 = l1.next
    # while l2:
    # 	l2_list.append(l2.val)
    # 	l2 = l2.next
    l1_len = len(l1_list)
    l2_len = len(l2_list)
    if l1_len == 0: return l2
    if l2_len == 0: return l1
    slen = l1_len if l1_len < l2_len else l2_len
    i = 0
    j = 0
    print(slen)
    while i<=slen-1 and j<=slen-1:
        print(f'i:{i}, j:{j}')
        if l1_list[i] == l2_list[j]:
            sorted_list += [l1_list[i], l1_list[j]]
            i += 1
            j += 1
        elif l1_list[i] < l2_list[j]:
            sorted_list.append(l1_list[i])
            i += 1
        else:
            sorted_list.append(l2_list[j])
            j += 1
        print('Sorted List after while: ', sorted_list)
    sorted_list += l1_list[i:]
    sorted_list += l2_list[j:]
    head = Node(sorted_list[0])
    prev_node = head
    print(sorted_list[0])
    for item in sorted_list[1:]:
        print(item)
        curr_node = Node(item)
        prev_node.next = curr_node
        prev_node = curr_node
    return head


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = node = ListNode(-1)

        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        node.next = l1 or l2

        return root.next

    def sortedLL(self, l1, l2):
        root = node = Node()
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 or l2
        return root.next

sortLL('', '')
