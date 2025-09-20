class Node():
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


class Stack():
    def __init__(self):
        self.top = Node(None)
        self.size = 0
    
    def push(self, value):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top

        self.size += 1

    def pop(self):
        top = self.top
        self.top = self.top.next

        self.size -= 1

        return top
    
    def is_empty(self):
        return self.size == 0
    

class Queue():
    def __init__(self):
        self.top = Node(None)
        self.end = Node(None)
        self.size = 0
    
    def push(self, value) -> None:
        new_end = Node(value)

        if self.end.data != None:
            self.end.next = new_end
        else:
            self.top = new_end
        self.end = new_end

        self.size += 1

    def pop(self) -> Node:
        top = self.top

        self.top = self.top.next
        if self.top == None:
            self.end = Node(None)

        self.size -= 1

        return top
    
    def is_empty(self):
        return self.size == 0
    

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




if __name__ == "__main__":
    ll = LinkedList()

    ll.push_left(3)
    ll.push_left(2)
    ll.push_left(1)

    ll.push_right(4)
    ll.push_right(5)
    ll.push_right(6)

    print(ll.pop_left().data)
    print(ll.pop_left().data)
    print(ll.pop_left().data)
    print(ll.pop_right().data)
    print(ll.pop_right().data)
    print(ll.pop_right().data)
