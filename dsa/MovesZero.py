# leatcode problem 283

nums = [1,0,3,4,2,0,0,1,2,5]

# 1. bruit force
# Time  O(n)
# Space O(n)  -- non zero list

non_zero = []
count = 0
for i in nums:
    if i != 0:
        non_zero.append(i)
    else:
        count += 1

nums[:] = non_zero + [0] * count

print(nums)

# 2. one-liner
# uses extra space
# Time:  O(n)
# Space: O(n) -- create new list

nums[:] = [x for x in nums if x != 0 ] + [0] * nums.count(0)
print(nums)



# 3. Two pointer
# Time:  O(n0)
# Space: O(1) -- No new list, no concatenation

pos = 0

for i in range(0,len(nums)):
     if nums[i] != 0:
        nums[pos], nums[i] = nums[i], nums[pos]
        pos += 1
print(nums)
