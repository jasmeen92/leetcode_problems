def jump(nums):
    jumps = 0
    end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == end:        # need to make a jump
            jumps += 1
            end = farthest  # move to next range

    return jumps
