def add(a,b,c):
    result = a+b+c
    return result

result = (lambda a,b,c: a+b+c)(3,4,5)
print(result)

square = lambda x: x **2
print(square(5))

square = lambda x=10: x**2
print(square())

data = [('Dianaaaa',30),('Ana',25), ('Tudor',22)]
data.sort() # will sort alphabetically
print (data)
data.sort(key=lambda x: x[1]) # creates a compare element at index 1 inside the tuple
print(data)
data.sort(key=lambda x: len(x[0])) # sort by len of the name

print(data)

#CHALLENGES
def unique_list(my_list):
    unique_elements = []
    for x in my_list:
        if x not in unique_elements:
            unique_elements.append(x)
    return unique_elements
list1 = [1,2,3,3,3,3,4,5,1,3,5,5,5]
print(unique_list(list1))


