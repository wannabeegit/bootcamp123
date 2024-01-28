# for loops

# for letter in 'Python': #
#     print(letter)
#     print('bye')
#     print('###')

# my_str = input('enter something')
# vowels = 'aeiou'
# for item in my_str:
#     if item in vowels:
#         print(item, end=' ')

#iterable is an object you can loop over (sets,list)


for i in range(1,100):
    if i % 3 and i % 5 == 0:
        print(f'fizzbuzz {i}')
    if i % 3 ==0:
        print(f'fizz {i}')
        if i % 5==0:
            print(f'buzz {i}')
