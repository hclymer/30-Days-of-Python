"""Bagels, by Al Sweigart al@inventwithpython.com
 2. A deductive logic game where you must guess a number based on clues.
 3. View this code at https://nostarch.com/big-book-small-python-projects
 4. A version of this game is featured in the book "Invent Your Own
 5. Computer Games with Python" https://nostarch.com/inventwithpython
 6. Tags: short, game, puzzle"""


import random


NUM_DIGITS = 5 
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
          by Al Sweigart al@!inventwithpython.com
          
          I am thinking of a {} -digit number with no repeated digits. 
          Try to guess what it is. Here are some lcues:
          when I say: That means:
          Pice         One digit is correct but in the wrong position.
          Fermi        One digit is correct and in the right position.
          Bagels       No digit is correct.
          for example if the secret number was 248 and you guess was 843, 
          the clues would be Fermi Pico.'''.format(NUM_DIGITS))
    
    while True: #main game loop
    #this stores the secret number
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(f"you have {MAX_GUESSES} to get it")
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}:")
                guess = input('> ')
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break 
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"the answer was {secretNum}.")
            
        print("do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print("Thanks for playing!")
    

def getSecretNum():
    numbers = list("0123456789")
    random.shuffle(numbers)
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return "you got it!"
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)
    
if __name__ == "__main__":
    main()
        