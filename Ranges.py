# RANGES

# r=range(2,10)
# print(type(r))
# print(list(r))
#
# #range(stop)
#
# print(list(range(10)))
# print(list(range(-20,10,4)))

#LOOPS AND RANGES

s=0
for n in range(101):
    s += n
print(f'Sum: {s}')

for _ in range(10):
    print('do something', _)

import random
names = ['Diana', 'paul', 'Dan', 'victor', 'harry', 'maria', 'Jeff', 'Angie']
for _ in range(3):
     print(f'choosing winner, Round {_}...')
     winner = random.choice(names)
     names.remove(winner)
     print(winner)
     print('###')
