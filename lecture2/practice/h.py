class Node(object):
    def __init__(self, val=0, next=None):
        self.val : int = val

        self.next: Node = next


def insert(head: Node, node: Node, p: int): # return new head of linked list
    if p != 0:
        l = head
        for _ in range(p - 1):
            l = l.next
    
        node.next = l.next
        l.next = node

        return head

    if p == 0:
        node.next = head

        return node

    
def remove(head: Node, p: int): # return new head of linked list
    if p != 0:
        prev = head
        for _ in range(p - 1):
            prev = prev.next
        
        prev.next = prev.next.next

        return head

    if p == 0:
        return head.next
    
 
def printAll(head: Node): # void function
    cur = head
    while cur != None:
        print(cur.val, end=" ")
        cur = cur.next
    print('')
    

def replace(head: Node, p1: int, p2: int): # return new head of linked list
    to_replace = head
    for _ in range(p1):
        to_replace = to_replace.next
    
    return insert(remove(head, p1), to_replace, p2)

 
def reverse(head: Node):  # return head of new linked list
    prev = None
    cur = head
    while cur != None:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    
    return prev

def cyclic_left(head: Node, x: int):  # return new head of linked list
    if x != 0:
        new_head = head
        prev = Node(None, head)
        for _ in range(x):
            new_head = new_head.next
            prev = prev.next
        
        prev.next = None

        end = new_head.next
        before_end = new_head

        while end != None:
            end = end.next
            before_end = before_end.next
        
        before_end.next = head

        return new_head
    
    if x == 0:
        return head

 
def cyclic_right(head: Node, x: int):   # return new head of linked list
    return reverse(cyclic_left(reverse(head), x))

 
 
head: Node = None
 
while(True):
    vals = [int(i) for i in input().split()]
    if (vals[0] == 0):
        break
    elif (vals[0] == 1):
        head = insert(head, Node(vals[1]), vals[2])
    elif (vals[0] == 2):
        head = remove(head, vals[1])
    elif (vals[0] == 3):
        printAll(head)
    elif (vals[0] == 4):
        head = replace(head, vals[1], vals[2])
    elif (vals[0] == 5):
        head = reverse(head)
    elif (vals[0] == 6):
        head = cyclic_left(head, vals[1])
    elif (vals[0] == 7):
        head = cyclic_right(head, vals[1])