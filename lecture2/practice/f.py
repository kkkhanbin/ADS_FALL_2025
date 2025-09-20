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
    
    def push_left(self, value: any) -> None:
        new_node = Node(value)

        if self.left.data == None and self.right.data == None:
            self.left = new_node
            self.right = new_node
        else:
            old_left = self.left
            self.left = new_node
            old_left.prev = new_node
            new_node.next = old_left
            new_before_left = Node(None)
            self.left.prev = new_before_left
            new_before_left.next = self.prev
        
        self.size += 1
        
    def push_right(self, value: any) -> None:
        new_node = Node(value)

        if self.left.data == None and self.right.data == None:
            self.left = new_node
            self.right = new_node
        else:
            old_right = self.right
            self.right = new_node
            old_right.next = new_node
            new_node.prev = old_right
            new_after_right = Node(None)
            new_node.next = new_after_right
            new_after_right.prev = self.right

        self.size += 1
    
    def pop_left(self) -> any:
        # there are only 1 element
        if self.left == self.right:
            popped = self.left

            self.left = Node(None)
            self.right = Node(None)

            return popped.data
        
        old_left = self.left
        self.left = old_left.next

        self.size -= 1

        return old_left.data

    def pop_right(self) -> any:
        # there are only 1 element
        if self.left == self.right:
            popped = self.right

            self.left = Node(None)
            self.right = Node(None)

            return popped.data
        
        old_right = self.right
        self.right = old_right.prev

        self.size -= 1

        return old_right.data


    def insert(self, value: any, index: int) -> None:
        new_value = Node(value)

        r = self.left
        for _ in range(index):
            r = r.next


        if r.prev == None:

            self.left = new_value
            new_value.next = r
            r.prev = new_value
        elif r.data == None:
            new_value.left = self.right
            new_after_right = Node(None)
            new_value.right = new_after_right
            new_after_right.prev = new_value
            self.right.next = new_value
            self.right = new_value
        else:

            l = r.prev
            
            l.next = new_value
            r.prev = new_value

            new_value.prev = l
            new_value.next = r

        self.size += 1


    def is_empty(self) -> bool:
        return self.size == 0


ll = LinkedList()
for _ in range(int(input())):
    ll.push_right(int(input()))
    # added = ll.pop_right()

    # print(added, end=" - ")

    # ll.push_right(added)

ll.insert(int(input()), int(input()))
for _ in range(ll.size):
    print(ll.pop_left(), end = " ")