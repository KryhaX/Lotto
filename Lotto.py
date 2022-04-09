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
        print('The winning numbers are: {}'.format(numbers))
        print(tprint('You_won_1,000,000$'))
    else:
        print('The winning numbers are: {} \nYou bet on: {}'.format(numbers, chosen_num))
        tprint('You_lose_:c')

# Compareing numbers
#print(numbers)
#print(chosen_num)
compare(numbers,chosen_num)



