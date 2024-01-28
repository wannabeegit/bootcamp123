# index and count
t1=(1,1,2,3,4)

#tuple.index()
x = 18
if x in t1:
    i = t1.index(x) #brings only the first occurance
    print(f'f is at index {i}')
else:
    print(f'{x} not in tuple')

# tuple.count()
n = t1.count(1)
print(n)

#len
print(len(t1))
print(sum(t1))
print(max(t1))
print(min(t1))

t2 = sorted(t1) #ascending order
print(t2)

t2= sorted(t1, reverse=True)
print(t2)