import collections

d1, d2 = collections.deque(), collections.deque()
s1, s2 = input().split()

for char in s1:
    if char == "#" and len(d1) > 0:
        d1.pop();
    else:
        d1.append(char)

for char in s2:
    if char == "#" and len(d2) > 0:
        d2.pop();
    else:
        d2.append(char)

print({True: "Yes", False: "No"}[d1 == d2])
