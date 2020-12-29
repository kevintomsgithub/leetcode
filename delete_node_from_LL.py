class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def make_the_LL(a):
    prev = head = Node(a[0])
    for i in a[1:]:
        curr = Node(i)
        prev.next = curr
        prev = curr
    return head
    
def display(head):
    while head:
        print(head.val, ' -> ', end='')
        head = head.next
    print('None')

def delete_node(head, n):
    prev = head
    curr = head.next
    while curr:
        if curr.val == n:
            prev.next = curr.next
            return
        prev = curr
        curr = curr.next

def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

a = [1, 2, 3, 4]
head = make_the_LL(a)
display(head)
# delete_node(head, 3)
rev_head = reverse(head)
display(rev_head)
rev_head = reverse(rev_head)
display(rev_head)
