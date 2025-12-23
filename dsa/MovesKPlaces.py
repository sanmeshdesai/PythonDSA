nums = [3, 9, 5, 6, 7, 2]

# k = 7
# r = k % len(nums)
# for _ in range(0, r):
#     e = nums.pop()
#     nums.insert(0, e)
#
# print(nums)

# k = 5
# n = len(nums)
# k = k % n
# nums[:] = nums[n-k:] + nums[:n-k]
# print(nums)

def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

reverse(nums, )