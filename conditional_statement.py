# conditional statements

balance = 100
price = 500

# if balance >= price:
#     new_balance = balance - price
#     print(f'you can book the flight and new balance will be{new_balance}')
#
# else:
#     print(f'Insufficient funds! Please deposit {price - balance}')
#
# print('Other instructions...')
# x = 10
# ...

answer = input('Do you want to continue? yes or no:').lower()
if answer == 'yes':
    print('we\'ll continue')
elif answer == 'no':
    print('we\'ll stop')
else:
    print('Invalid answer')

