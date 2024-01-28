# def all_divisors(n):
#     """
#      This function returns all divisors of a number
#     """
#     divisors = []
#     for x in range(1, int(n/2)+1):
#         if n % x == 0:
#             divisors.append(x)
#     return divisors
#
# def perfect_nums(n):
#     divs = all_divisors(n)
#     if sum(divs) == n:
#         return True
#     else:
#         return False
#
# n = range(0,1000)
# if perfect_nums(n):
#     print(f'{n} is a perfect number')

#BMI CALCULATOR
name1='Dave'
height1 = 2
weight1 = 90

name2 = 'Dave\'s sister'
height2 = 1.8
weight2 = 70

name3 = 'Dave\'s brother'
height3 = 2.5
weight3 = 70

def bmi_calc(name, height,weight):
    bmi = weight/(height**2)
    print('BMI: ')
    print(f'{bmi:.2f}')
    if bmi <25:
        print(name + ' is not overweight')
    else:
        print(name + ' is overweight')

reult1 = bmi_calc(name1, height1,weight1)
reult1 = bmi_calc(name2, height2,weight2)
reult1 = bmi_calc(name3, height3,weight3)

num = int(input('Enter number: '))
print(f'Multiplication table for {num}')
for i in range(0,11):
    result = i * num
    print(f'{num} X {i} = {result}')