class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.float_up(len(self.heap)-1)
    
    def push(self, data):
        self.heap.append(data)
        self.float_up(len(self.heap)-1)
    
    def peek(self):
        return self.heap[1] if self.heap[1] else False

    def pop(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap)-1)
            max_val = self.heap.pop()
            self.bubble_down(1)
        elif len(self.heap) == 2:
            max_val = self.heap.pop()
        else:
            max_val = False
        return max_val

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def float_up(self, index):
        if index <= 1:
            return
        parent = index//2
        if self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.float_up(parent)

    def bubble_down(self, index):
        parent = index
        left = index * 2
        right = index * 2 + 1
        if len(self.heap) > left and self.heap[parent] < self.heap[left]:
            parent = left
        if len(self.heap) > right and self.heap[parent] < self.heap[right]:
            parent = right
        if parent != index:
            self.swap(index, parent)
            self.bubble_down(parent)

m = MaxHeap([-1, -14, -15, -19])
m.push(-123)
print(m.heap[1:])
print(m.pop())
print(m.peek())