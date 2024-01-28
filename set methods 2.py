
s1 = {1,3,5}
s2 = {5,7,9}

#1. set.intersection
s3 = s1.intersection(s2)
print(s3) #or
s3 = s1 & s2
print(s3)

#2. set.difference
s4 = s1.difference(s2)
print(s4) #or
s4 = s1-s2
print(s4)

#3. set.symmetric_difference()
s5 = s1.symmetric_difference(s2)
print(s5) #or
s5 = s1 ^ s2
print(s5)

#4. set. union() set of all unique elements within the 2 sets
s6 = s1.union(s2)
print(s6 )

# set.isdisjoint() if they have no elements in common
set1 = {1,3,5}
set2 = {5,6,7}
print(set1.isdisjoint(set2))
set3 = {8,9}
print(set1.isdisjoint(set3))