def reverse(nums,l,r):
   while l < r:
       nums[l], nums[r] = nums[r], nums[l]
       l += 1
       r -= 1
   return nums

nums = [1,2,3,4,5,6,7,8,9]

print(reverse(nums,0,len(nums)-1))