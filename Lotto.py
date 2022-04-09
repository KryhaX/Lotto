import random
from art import *
tprint('Lotto!')

numbers = []

for n in range(1,11):
    random_num = n
    random_num = random.randrange(1,10)
    numbers.append(random_num)

#print(numbers) # Won list of numbers
chosen_num = []

for num in range(1,11):
    choice = int(input("Give me {} bet number: ".format(num)))
    chosen_num.append(choice)

def compare(l1,l2):
    set(l1)
    set(l2)
    if l1 == l2:
        print(tprint('You_won_1,000,000$'))
    else:
        tprint('You_lose_:c')
        print('The winning numbers are:')
        print(numbers)

# Compared numbers
#print(numbers)
#print(chosen_num)
compare(numbers,chosen_num)

