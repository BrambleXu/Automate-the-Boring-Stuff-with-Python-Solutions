# This is a guess the number game.
import random
secret_number = random.randint(1, 20)
print ('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print ('take a guess.')
    guess = int(input())

    if guess < secret_number:
        print ('Your guess is too low.')
    elif guess > secret_number:
        print ('Your guess is too high.')
    else:
        break  # This condition is the correct guess!

if guess == secret_number:
    print ('Good job! You guessd my number in ' + str(guesses_taken) + ' guesses!')
else:
    print ('Nope. The number I was thinking of was ' + str(secret_number))
