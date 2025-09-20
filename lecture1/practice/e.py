from queue import Queue

a = Queue()
b = Queue()

for card in map(int, input().split()):
    a.put(card)
for card in map(int, input().split()):
    b.put(card)

i = 1
while True:
    if i >= 10 ** 6:
        print("blin nichya")
        break

    a_card = a.get()
    b_card = b.get()

    if a_card == 0 and b_card == 9:
        a.put(a_card)
        a.put(b_card)
    elif b_card == 0 and a_card == 9:
        b.put(a_card)
        b.put(b_card)

    elif a_card > b_card:
        a.put(a_card)
        a.put(b_card)
    else:
        b.put(a_card)
        b.put(b_card)

    if a.empty():
        print("Nursik", i)
        break
    elif b.empty():
        print("Boris", i)
        break

    i += 1
