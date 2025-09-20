n = int(input())

nums = [True for _ in range(10000)]

i = 2
while i * i <= 9000:
    for j in range(i + i, 9000, i):
        nums[j] = False
    i+=1

print(list(filter(lambda num: num[1], enumerate(nums)))[n + 1][0])

