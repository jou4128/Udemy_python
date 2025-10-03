'''
random module:
1. random.random() 
    return a random float between 0.0 and 1.0
2. random.uniform(x, y)
    return a random float between x and y
3. random.randint(x, y)
    return a random integer between x and y
'''

import random

target_num = random.randint(1, 100)
print(target_num)
min_value = 1
max_value = 100

while True:
    guess = input(f"Guess a number between {min_value} and {max_value}: ")

    if int(guess) < min_value or int(guess) > max_value:
        print("Your number is out of range!")
        continue

    if int(guess) == target_num:
        print(f"You WIN! The secret number is {target_num}.")
        break
    elif int(guess) < target_num:
        min_value = int(guess)
    elif int(guess) > target_num:
        max_value = int(guess)
