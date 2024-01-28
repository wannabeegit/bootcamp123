# tuples are immutable

t1=tuple()
t2= ()
print(type(t1), type(t2))

#TUPLE OPERATIONS

my_tuple = (1.2, 12,'abc', True,(30,40),'x')
t1 = my_tuple + tuple('yz')
print(t1)

t2 = (1,2,'a') * 3
print(t2)
print(my_tuple[0:2])
print(my_tuple[:3])
print(my_tuple[2:])
print(my_tuple[::])
print(my_tuple[::2])
print(my_tuple[-1:0:-1])