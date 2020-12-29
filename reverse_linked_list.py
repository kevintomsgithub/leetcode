class Node:
    def __init__(self, val=None):
        self.val = val
        self.link = None

def make_the_LL():
    head = prev = Node(0)
    for i in range(1, 11):
        n = Node(i)
        prev.link = n
        prev = n
    return head

def get_end(node):
    while node:
        if node.link == None: return node
        node = node.link

def display(node):
    while node:
        print(node.val)
        node = node.link

def reverse_LL(node):
    prev = None
    curr = node
    while curr:
        next = curr.link
        curr.link = prev
        prev = curr
        curr = next
    return prev

def reverse_LL_rec(node):
    if node == None or node.link == None: return node
    last_node = reverse_LL_rec(node.link)
    last_node.link = node
    node.link = None
    return node
 
head = make_the_LL()
end = get_end(head)
display(end)
rev_head = reverse_LL(head)
rev_rec_head = reverse_LL_rec(head)
display(end)
# display(head)