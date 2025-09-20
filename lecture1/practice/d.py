from collections import deque
from string import ascii_lowercase

s = input()

count = dict()
for char in ascii_lowercase:
    count[char] = 0

deq = deque()

passed = "YES"
for char in s:
    if len(deq) == 0:
        deq.append(char)
        count[char] += 1
        continue

    last = deq.pop()

    if count[char] != 0 and char == last:
        count[char] -= 1
    else:
        deq.append(last)
        deq.append(char)

        count[char] += 1
    


if len(deq) != 0:
    print("NO")
else:
    print(passed)
