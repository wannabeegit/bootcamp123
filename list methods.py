# list methods

# adding to the list: append()- adds single element to end of list.
# extend()-adds all elements of iterable object tp en of the list,
# Insert()- inserts element at a specific index in a list

l1=[1,2,3,'abc']
l1.append(6)
print(l1)

l1.extend('h')
print(l1)

years = [2020,2022,2023]
years.insert(1,2021)
print(years)
years.insert(len(years), 2024)# inserts at the end of the list
print(years)
years.insert(-1, 2025) # inserts at 2nd last position
print(years)

#list clear
years.clear()
print(years)

# list.pop removes element at given index, removes last by default
l2=[1,2,3,4]
x=l2.pop()
print(x) # will return the last value
print(l2)

y=l2.pop(1)
print(y,l2) #out of range index will return error

# list.remove
l3= [10,20,10,40,20,10,20]
l3.remove(10)
print(l3) #removes only the first element of 10
while 20 in l3:
    l3.remove(20)
print(l3)