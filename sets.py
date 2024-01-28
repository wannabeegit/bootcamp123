# SET METHODS

s1= {1,2,3}
s1.add('a')
s1.add('4.5')
print(s1)

#2. set.remove(item)
s1.remove(3)
print(s1)

#3. set.discard(item)
s1.discard('a')
print(s1)

#4. set.pop() pop takes no argument, returns a random element from the froup
x = s1.pop()
print(x, s1)

#5. set.clear() will clear all elements in a set

