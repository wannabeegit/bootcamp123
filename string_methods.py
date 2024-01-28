# STRING METHODS
#

my_str = 'I learn python Programming'

# 1 str.upper()
print(my_str.upper())

# str.strip - eliminates white spaces or any values before var
ip = '  192.168.0.2  '
print(ip)
ip = ip.strip()
print(ip)
value = '$$76664$$'
print(value.strip('$'))

# SRT.REPLACE()
new_value = value.replace('$' , '@')
print(new_value)

# str.count()
txt = 'i learn Python python programming'
n = txt.count('python')
print(n)
n = txt.lower().count('python')
print(n)

# str.split()

my_list = txt.split()
print(my_list)

print('2.23.4.65'.split('.'))

# str.join()

ip = '10.2.1.4'
ip_list = ip.split('.')
print(ip_list)

ip_str = '.'.join(ip_list) # joins iplist with a . symbol

# str.find()
print('Python'.lower() in my_str)

s1 = 'mom'
print(f'is s1 palindrome? => {s1 == s1[::-1]}')

