nums = [0,1]


n = len(nums)
sum = n * ( n + 1)/2

sumlist = 0

for i in nums:
    sumlist = sumlist +  i

print(sumlist)

m = sum - sumlist
print(m)



#
# for i in range(0,lens+1):
#     if i not in nums:
#         print(i);


# mydict = dict.fromkeys(range(len(nums)+1),0)
#
#
# for n in nums:
#     mydict[n] = 1
#
# for key, value in mydict.items():
#     if value == 0:
#         print(key)
