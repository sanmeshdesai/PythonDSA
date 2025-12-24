nums = [2, 1, 4, 8, 5, 7, 9, 6]

# average/ worst case
def bubble_sort(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

print(bubble_sort(nums))


nums1 =[1,2,3,4,5,6,7,8]
#best case
def bubble_sort2(nums):
    n = len(nums)
    is_swap = False
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if not is_swap:
            break
    return nums


print(bubble_sort2(nums1))



