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


names = Stack()
for _ in range(int(input())):
    new_name = input()
    prev = names.pop()
    if prev.data != new_name:
        names.push(prev.data)
        names.push(new_name)
    else:
        names.push(prev.data)
    
print(f"All in all: {names.size}\nStudents:")
while not names.is_empty():
    print(names.pop().data)