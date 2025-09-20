for _ in range(int(input())):
    input()

    letters = [None for _ in range(26)]
    added = set()
    order = 0
    for char in input().split():
        if char not in added:
            order += 1
            added.add(char)

        i = ord(char) - ord('a')
        if letters[i] is None:
            letters[i] = order
        elif letters[i] is not None:
            letters[i] = False

        key = min(letters, key=lambda x: x if x is not None and x is not False else 999)
        # print(letters, key)
        if key is False or key is None:
            print("-1", end=" ")
        else:
            print(chr(letters.index(key) + ord('a')), end=" ")
    
    print()
