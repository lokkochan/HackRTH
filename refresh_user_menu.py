#user menu
import random

def print_menu():
    distance = 0
    num_stairs = 0
    num_pushups = 0
    action = ''
    diff1 = random.randint(1,6)
    diff2 = random.randint(1,6)
    diff3 = random.randint(1,6)
    
    if (diff1 > 3 and diff2 > 3 and diff3 > 3):
        diff1 = random.randint(1,6)
        diff2 = random.randint(1,6)
        diff3 = random.randint(1,6)

    if diff1 == 1:
        distance = 1
        action = 'Walk'
    elif diff1 == 2:
        distance = 3
        action = 'Walk'
    elif diff1 == 3:
        distance = 5
        action = 'Walk'
    elif diff1 == 4:
        distance = 1
        action = 'Run'
    elif diff1 == 5:
        distance = 3
        action = 'Run'
    elif diff1 == 6:
        distance = 5
        action = 'Run'

    if diff2 == 1:
        num_stairs = 10 * diff2
    elif diff2 == 2:
        num_stairs = 10 * diff2
    elif diff2 ==3:
        num_stairs = 10 * diff2
    elif diff2 ==4:
        num_stairs = 10 * diff2
    elif diff2 ==5:
        num_stairs = 10 * diff2
    elif diff2 ==6:
        num_stairs = 10 * diff2

    if diff3 == 1:
        num_stairs = 5 * diff3
    elif diff3 == 2:
        num_stairs = 5 * diff3
    elif diff3 ==3:
        num_stairs = 5 * diff3
    elif diff3 ==4:
        num_stairs =  5 * diff3
    elif diff3 ==5:
        num_stairs = 5 * diff3
    elif diff3 ==6:
        num_stairs = 5 * diff3

    option1 = f'{action} {distance} km.'

    option2 = f'Climb {num_stairs} stairs'

    option3 = f'Do {num_pushups} pushups'
    
    print(f'Tasks for today: \n1.{option1}\n2. {option2}\n3. {option3}')


