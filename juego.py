import random

options = ('stone', 'paper', 'scissors')
options2 = {1:'stone', 2:'paper', 3:'scissors'}

user_option = input('Enter option 1. stone 2. paper 3. scissors: ')


if user_option.isdigit() == True:
    user_option = str(options2.get(int(user_option)))

user_option = user_option.lower()
if not user_option in options:
    print('Invalid option')
computer_option = random.choice(options)


print(f"user option: {user_option}")
print(f'computer option: {computer_option}')




