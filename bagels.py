import random

NUM_DIGITS = 3
MAX_GUESSES = 15

def main():
    print(
        '''Bagels, a deductive logic game.
        I am thinking of a {}-digit number with no repeated digits.
        Try to guess what it is. Here are some clues:
        When I say:     That means:
        Yellow:         One digit is correct but in the wrong position.
        Green:          One digit is correct and in the right position.
        Red:            No digit is correct.
        For example, if the secret number was 248 and your guess was 843, 
        the clues would be Yellow Green.'''.format(NUM_DIGITS))

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Creates a list of digits 0 to 9
    random.shuffle(numbers) # Shuffles numbers in random order

    # Get the first NUM_DIGITS digits in the list for the secret number
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the red, yellow, green clues
    for a guess and secret number pair"""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Green')
        elif guess[i] in secretNum:
            clues.append('Yellow')
    if len(clues) == 0:
        # There are no correct digits at all
        return 'Red'
    else:
        # Sort clues into alphabetical order so their original order doesn't
        # give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)

if __name__ == '__main__':
    main()

while True: # main game loop (stores secret number)
    secretNum = getSecretNum()
    print('I have thought up a number.')
    print('You have {} guesses to get it.'.format(MAX_GUESSES))

    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        guess = ''
        # Keeps it looping until they enter a valid guess. 
        # Len function returns number of items in an object
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print('Guess #{}: '.format(numGuesses))
            guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
    
    # Ask player if they want to play again
    print('Do you want to play again? (yes/no)')
    if not input('> ').lower().startswith('y'):
        break

print('Thanks for playing!')