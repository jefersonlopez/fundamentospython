import random


options = ('stone', 'paper', 'scissors')
options2 = {1:'stone', 2:'paper', 3:'scissors'}

rounds = int(input('How many rounds you want to play: '))
loop = 0
computer_wins = 0
user_wins = 0
tie = 0
wins = (rounds // 2) + 1
print(wins) 

while True:

    print('*-' * 15)
    print('ROUND ', loop + 1)
    print('*-' * 15)
    user_option = input('Enter option 1. stone 2. paper 3. scissors: ')
    computer_option = random.choice(options)

    if user_option.isdigit() == True:
        user_option = str(options2.get(int(user_option)))

    user_option = user_option.lower()
    if not user_option in options:
        print('Invalid option')
        continue   
    elif user_option == computer_option:
        print("Tie")
        tie += 1
    elif user_option == 'stone' and computer_option == 'scissors':
        print('user win')
        user_wins += 1
    elif user_option == 'scissors' and computer_option == 'paper':
        print('user win')
        user_wins += 1
    elif user_option == 'paper' and computer_option == 'stone':
        print('user win')
        user_wins += 1
    else:
        print('computer win')
        computer_wins += 1

    print(f"user option: {user_option}")
    print(f'computer option: {computer_option}')
    loop += 1
    
    if loop >= wins:
        if user_wins != computer_wins or user_wins >= wins or computer_wins >= wins:
            break
print('-' * 40) 
print('finish') 
if user_wins > computer_wins:
    print('********************************')
    print('* WIN WIN WIN USER WIN WIN WIN *')
    print('********************************')
else:
    print('************************************')
    print('* WIN WIN WIN COMPUTER WIN WIN WIN *')
    print('************************************')
print('user wins:', user_wins)
print('computer wins:', computer_wins)
print('tie: ', tie)
print('-' * 40) 

