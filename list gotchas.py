l1 = [1,2,3]
l2=l1
l2[0] = ['xx']
print(l1,l2,id(l1),id(l2))

l3 = l1.copy()
l3.append('abc')
print(l1,l3)

# 2 to remove numbers <5
nums = [1,2,3,4,5,6,7,0,1,2]
#wrong method
for n in nums: # you shouldn't iterate a list while looping over it
    if n<5:
        nums.remove(n)
print(nums)

#right way
new_list= list()
for n in nums:
    if n>=5:
        new_list.append(n)
print(new_list)

#or
my_list = [n for n in nums if n>=5]
print(my_list)