# *args used for positional arguments
# def average(a,b,*args):
#     return (a+b + sum(args))/(2+len(args))
#
# def concatenate(*args):
#     result= ''
#     for tmp in args:
#         result = result + tmp
#     return result
# r = concatenate('i', ' love', ' programming')
# print(r)

# **kwargs
def my_function(**kwargs): # ** for keyword arguments
    print(kwargs)
    for k, v in kwargs.items():
        print(f'k is {k} and v is {v}')
my_function(name='john', age=40, location='london')
person = {'name': 'Adreas', 'age': 30, 'location': 'Berlin'}
my_function(**person)