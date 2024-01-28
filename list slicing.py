
numbers = [1,2,3,4,5]
nums = numbers[1:4]
print(f'nums: {nums}')
print(f'numbers: {numbers}')
print(numbers[:3]) #all index from 0 includes to 3 excluded
print(numbers[2:]) # stop is default to end of the list
print(numbers[1:5:3])
print(numbers[4:1:-2])
print(numbers[::]) # this is copy os the list
print(numbers[::-1]) #this will reverse the numbers
numbers[0:2] = ['a','b'] # replaces the index with new ones
print(numbers)
numbers[0:2] = ['x','y','z']
print(numbers)

# LIST ITERATION

ip_list=['192.168.0.1', '192.168.0.2', '10.0.0.1']
for ip in ip_list:
    print(f'connecting to {ip} ...') # iteration

print('10.0.0.1' in ip_list)# true /testing list membership
print('192' not in ip_list)

#
