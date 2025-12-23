nums = [1,5,3,6,7,9,3,2]

def selection_sort_desc(nums):
    n = len(nums)

    for i in range(n):
        max_index = i
        for j in range(i+1,n):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[max_index], nums[i] = nums[i], nums[max_index]
    return nums

print(selection_sort_desc(nums))