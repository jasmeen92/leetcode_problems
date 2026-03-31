def rotate(nums, k):
    n = len(nums)
    k = k % n  # handle k > n

    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    # Step 1: reverse whole array
    reverse(0, n - 1)

    # Step 2: reverse first k elements
    reverse(0, k - 1)

    # Step 3: reverse remaining
    reverse(k, n - 1)
