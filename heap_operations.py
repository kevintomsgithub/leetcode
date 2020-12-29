# Min heap
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

class Heap:
    def __init__(self, array):
        self.heap = []
        self.root = None
        self.heapify(array)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _get_parent(self, index):
        parent_index = (index-1)//2
        if parent_index >= 0:
            return {
                'exist': True,
                'index': parent_index,
                'item': self.heap[parent_index]
            }
        else:
            return {
                'exist': False
            }


    def _get_right_child(self, index):
        right_index = (2 * index) + 1
        if right_index < len(self.heap):
            return {
                'exist': True,
                'index': right_index,
                'item': self.heap[right_index]
            }
        else:
            return {
                'exist': False
            }

    def _get_left_child(self, index):
        left_index = (2 * index)
        if left_index < len(self.heap):
            return {
                'exist': True,
                'index': left_index,
                'item': self.heap[left_index]
            }
        else:
            return {
                'exist': False
            }

    def _heap_up(self):
        index = len(self.heap)-1
        while self._get_parent(index)['exist']:
            parent = self._get_parent(index)
            if parent['exist'] and self.heap[index] < parent['item']:
                self.swap(index, parent['index'])
                index = parent['index']
            else:
                break

    def _heap_down(self):
        index = 0
        while self._get_left_child(index)['exist']:
            smaller_child = None
            right_child = self._get_right_child(index) 
            left_child = self._get_left_child(index)
            
            if right_child['exist'] and right_child['item'] < left_child['item']:
                smaller_child = right_child
            else:
                smaller_child = left_child
            
            if self.heap[index] < smaller_child['item']:
                break
            else:
                self.swap(index, smaller_child['index'])
                index = smaller_child['index']
        
    def add(self, x):
        self.heap.append(x)
        self._heap_up()

    def peek(self):
        if len(self.heap) == 0: return None
        return self.heap[0]

    def pop(self):
        if len(self.heap) == 0: return None
        self.swap(0, len(self.heap)-1)
        item = self.heap.pop()
        self._heap_down()
        return item

    def heapify(self, array):
        for i in array:
            self.add(i)

    def show(self):
        return self.heap

    # def convert_to_tree(self):
    #     if len(self.heap) == 0: return None
    #     self.root = Node(self.heap[0])
    #     index = 0
    #     parent = None
    #     while index < len(self.heap):
    #         node = Node(self.heap[index])
    #         left_node = self._get_left_child(index)
    #         right_node = self._get_right_child(index)
    #         if right_node['exist']:
    #             node.left = left_node['item']
    #             node.right = right_node['item']
    #         else:
    #             node.left = left_node['item']
    #         parent.
    #         if parent.left == None:
    #         if parent.right == None:
    #             parent.right = node
    #             parent = node
    #         index += 1


a = [5, 2, 1, 4, 3]
print(a)
heap = Heap(a)
print(heap.show())

