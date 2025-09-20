n = int(input())

nums = [[i, True] for i in range(10000)]

i = 2
while i * i <= 9000:
    for j in range(i + i, 9000, i):
        nums[j][1] = False
    i+=1

nums = list(filter(lambda num: num[1], nums[1:]))
length = len(nums)

i = 2
while i * i <= length:
    for j in range(i + i, length, i):
        nums[j][1] = False
    i+=1

print(list(filter(lambda num: num[1], nums))[n + 1][0])
