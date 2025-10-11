class HeapTree:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, value):
        self.heap.append(value)

        cur_i = len(self.heap) - 1
        parent_i = self.get_parent_index(cur_i)
        while parent_i is not None and self.heap[parent_i] < value:
            self.swap(cur_i, parent_i)
            cur_i, parent_i = parent_i, self.get_parent_index(parent_i)
            
    def get_parent_index(self, i):
        return (i - 1) // 2 if i != 0 else None
    
    def get_left_child_index(self, i):
        return 2 * i + 1
    
    def get_right_child_index(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def extract_max(self):
        max_num = self.heap[0]
        del self.heap[0]
    
        if len(self.heap) == 0:
            return max_num

        self.heap.insert(0, self.heap[-1])
        del self.heap[-1]

        cur_i = 0
        while True:
            l, r = self.get_left_child_index(cur_i), self.get_right_child_index(cur_i)
            largest = cur_i
            size = len(self.heap)

            if l < size and self.heap[l] > self.heap[largest]:
                largest = l

            if r < size and self.heap[r] > self.heap[largest]:
                largest = r

            if largest == cur_i:
                break

            self.swap(largest, cur_i)
            cur_i = largest

        return max_num