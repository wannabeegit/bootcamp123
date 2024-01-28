# PYTHON LISTS

l1 = [1, 2.5, 'python', 'files',['abc', 'xyz'], (10, 30, 20)]
print(len(l1))
l2=[]  #empty list
l3 = list() # empty list
x=l1[-1]
print(x)

# s1 = 'abc'
# s1[0] = 'x' #str is immutable

l4=list('abcd')
print(l4)
print(id(l4))
l4[0] = 'X'
l4.append(100)
print(l4)
print(id(l4))