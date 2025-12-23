nums = [1,1,1,0,1,0,1,0,1,0,1,1]

count = 0

m = 0

for i in nums:
    if i == 1:
        count += 1
        m = max(m,count)
    else:
        count = 0

print(m)

