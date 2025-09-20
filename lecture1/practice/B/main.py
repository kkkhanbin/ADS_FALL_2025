import collections

int(input())
nums = list(map(int, input().split()))

# people = collections.deque()

out = list()
for n in nums:
    out.append(n)

    for_print = -1

    for i in range(len(out) - 2, -1, -1):
        if out[i] <= n:
            for_print = out[i]
            break
    print(for_print, end=" ")
