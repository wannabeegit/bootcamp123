# for, else and break statements

for number in range(10):
    print(number)
    if number == 5:
        break

print('outside for')

for letter in 'Python':
    if letter == 'o':
        print('letter is o and I\'m breaking out of the loop')
        break
    print(letter)

for n in range (1,20):
    if n % 13 == 0:
        print('there is a number divisible by 13')
        break
else:
    print('there is no number divisible by 13')

for l in 'abc':
    print(l)
    for n in range(3):
        if n == 1:
            break
        print(n)