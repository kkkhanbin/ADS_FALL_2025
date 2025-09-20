import queue

for _ in range(int(input())):
    n = int(input())
    cards = queue.Queue(n + 1)

    for i in range(n, 0, -1):
        cards.put(i)
        for j in range(i, 0, -1):
            cards.put(cards.get())

    omg = []
    while not cards.empty():
        omg.append(cards.get())
    print(" ".join(map(str, reversed(omg))))
