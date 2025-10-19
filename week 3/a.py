n = int(input())
to_find = list(map(int, input().split()))
height, width = list(map(int, input().split()))

nums = []
for i in range(height):
    if (height - i) % 2 == 1:
        nums += list(map(lambda x: (int(x[1]), i, x[0]), enumerate(input().split())))
    else:
        nums += list(map(lambda x: (int(x[1]), i, x[0]), reversed(list(enumerate(input().split())))))


def bin_search(to_find: int, nums: list) -> list:
    if len(nums) == 1:
        if nums[0][0] == to_find:
            return [nums[0][1], nums[0][2]]
        return [-1]
    
    medium_i = len(nums) // 2

    if to_find <= nums[medium_i][0]:
        return bin_search(to_find, nums[medium_i:])
    return bin_search(to_find, nums[:medium_i])


for num_to_find in to_find:
    print(" ".join(map(str, bin_search(num_to_find, nums))))
