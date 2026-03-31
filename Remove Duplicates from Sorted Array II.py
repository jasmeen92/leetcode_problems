def removeDuplicates(nums):
    i = 0  # position to insert

    for num in nums:
        if i < 2 or num != nums[i - 2]:
            nums[i] = num
            i += 1

    return i
