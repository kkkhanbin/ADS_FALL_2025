from collections import deque

n = int(input())
s, k = deque(), deque()
inp = input()
for i in range(len(inp)):
    if inp[i] == "S":
        s.append(i)
    else:
        k.append(i)

s_count, k_count = inp.count("S"), inp.count("K")

while s_count > 0 and k_count > 0:
    s_vote, k_vote = s.popleft(), k.popleft()

    if s_vote < k_vote:
        s.append(s_vote + n)
        k_count -= 1
    else:
        k.append(k_vote + n)
        s_count -= 1

if len(s) == 0:
    print("KATSURAGI")
else:
    print("SAKAYANAGI")
