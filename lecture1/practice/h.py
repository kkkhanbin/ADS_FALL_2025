n = int(input())

nums = [True for _ in range(n + 100)]

i = 2
while i * i <= n + 100:
    nums[i * i:n + 100:i] = False
    for j in range(i + i, n + 100, i):
        nums[j][1] = False
    i+=1

nums[0] = False
nums[1] = False

print({True: "YES", False: "NO"}[nums[n][1]])

