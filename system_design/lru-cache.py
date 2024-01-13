
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data):
        # create a new node
        new_node = Node(data)
        
        # if created node if first the return
        if self.head == None:
            self.head = new_node
            return new_node
        
        # start from head
        current = self.head
        # traverse to the end
        while current.next:
            current = current.next
        # add links to the new node
        current.next = new_node
        new_node.prev = current
        return new_node
            
    def prepend(self, data):
        # create a new node
        new_node = Node(data)
        
        # if created node if first the return
        if self.head == None:
            self.head = new_node
            return new_node
        
        # replacing the head with the new node
        current = self.head
        self.head = new_node
        # adding links to the new node
        current.prev = new_node
        new_node.next = current
        return new_node
    
    # print the doubly linked list
    def __repr__(self) -> str:
        current = self.head
        return_str = "\n"
        while current:
            return_str += str(current.data) + '\n'
            current = current.next
        return return_str


class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache:
    
    def __init__(self, max_len=3) -> None:
        self.cache = {}
        self.head = None
        self.tail = None
        self.size = -1
        self.max_len = max_len
    
    def get(self, key):
        
        if key not in self.cache:
            return "Key not found in cache"
        
        current = self.cache[key]
        self.tail.next = current
        self.tail.prev = current.prev
        current.prev = self.tail
        current.next = None
        self.tail = current
        
        return current.value
    
    def put(self, key, value):
        
        if key in self.cache:
            print('Key already exist!')
            return
        
        # add elements
        self.size += 1
        new_node = Node(key, value)
        # add to cache
        self.cache[key] = new_node
        
        # for first value
        if self.head == None:
            # check if memory available
            if self.max_len <= 0:
                print('No memory allocated to cache!')
                return 
            self.head = new_node
            self.tail = new_node
            return

        # update tail object
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        
        if self.size >= self.max_len:
            # pop an element from cache
            self.cache.pop(self.head.key)
            # move head
            self.head = self.head.next
            self.head.prev = None
            
            
    

# dll = DoublyLinkedList()
# dll.prepend(1)
# dll.append(2)
# dll.append(3)
# dll.append(4)
# dll.append(5)
# dll.prepend(0)

# print(dll)

lru_cache = LRUCache(max_len=2)
lru_cache.put(1, 'Kevin')
lru_cache.put(2, 'Nevin')
lru_cache.put(3, 'Toms')
# lru_cache.put(4, 'aa')
# lru_cache.put(5, 'bb')