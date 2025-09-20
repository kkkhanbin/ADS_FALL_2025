from collections import deque
import sys

s = deque()

for line in sys.stdin.readlines():
    op = line[0]

    match op:
        case "+":
            s.appendleft(int(line[2:]))
        case "-":
            s.append(int(line[2:]))
        case "*":
            if len(s) == 0:
                print("error")
            elif len(s) == 1:
                print(s.pop() * 2)
            else:
                print(s.pop() + s.popleft())
