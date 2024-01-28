
# name := expression
print(x:=2+3)
print(f'x is {x}')

# print (y=10)

# value = input('enter something: ')
# while value != '':
#     print(f'you entered {value}')
#     value=input('enter something: ')

# while(value:=input('enter something: ')) !='':
#     print(f'you entered {value}')

# data = input('enter your name: ')
# if len(data) > 0:
#     print(f'your name has {len(data)} chars.')
# else:
#     print('name cannot be empty')

data = input('enter your name: ')
if (n:=len(data)) > 0:
    print(f'your name has {n} chars.')
else:
    print('name cannot be empty')