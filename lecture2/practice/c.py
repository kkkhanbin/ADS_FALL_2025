class Node():
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


class LinkedList():
    def __init__(self):
        self.left = Node(None)
        self.right = Node(None)

        self.size = 0
    
    def push_left(self, value: Node) -> None:
        new_node = Node(value)

        if self.left.data == None and self.right.data == None:
            self.left = new_node
            self.right = new_node
        else:
            old_left = self.left
            self.left = new_node
            old_left.prev = new_node
            new_node.next = old_left
        
        self.size += 1
        
    def push_right(self, value: Node) -> None:
        new_node = Node(value)

        if self.left.data == None and self.right.data == None:
            self.left = new_node
            self.right = new_node
        else:
            old_right = self.right
            self.right = new_node
            old_right.next = new_node
            new_node.prev = old_right

        self.size += 1
    
    def pop_left(self) -> None:
        # there are only 1 element
        if self.left == self.right:
            popped = self.left

            self.left = Node(None)
            self.right = Node(None)

            return popped
        
        old_left = self.left
        self.left = old_left.next

        self.size -= 1

        return old_left

    def pop_right(self) -> None:
        # there are only 1 element
        if self.left == self.right:
            popped = self.right

            self.left = Node(None)
            self.right = Node(None)

            return popped
        
        old_right = self.right
        self.right = old_right.prev

        self.size -= 1

        return old_right

    def is_empty(self) -> bool:
        return self.size == 0


n = int(input())
nums = list(map(int, input().split()))
ll = LinkedList()
for i in range(n):
    if i % 2 == 0:
        ll.push_right(nums[i])

while not ll.is_empty():
    val = ll.pop_left().data
    if val != None:
        print(val, end=" ")
