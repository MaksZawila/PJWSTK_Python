def print_numbers(n, ascending=True):
    nums = []
    i = 2
    while len(nums) < n:
        if i % 2 == 0 and i % 3 != 0:
            nums.append(i)
        i += 1

    mode = lambda x: x if ascending else -x
    nums.sort(key=mode)

    print(nums)


print_numbers(2, False)
